from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ValidationError
from django_zarinpal.services import start_transaction, verify_transaction
from django.core.mail import send_mail
from django_zarinpal.exceptions import ZarinpalException
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django import forms
from .models import *
import requests
import json


# Main Views
def web(request):
    setting_web = Setting_Web.objects.first()
    product = Product.objects.get(type='web')
    return render(request, 'home/web/index.html', {
        'product': product,
        'discount': Discount.objects.get(product=product),
        'setting_web': setting_web
    })


def ai(request):
    setting_ai = Setting_AI.objects.first()
    product = Product.objects.get(type='ai')
    return render(request, 'home/ai/index.html', {
        'product': product,
        'discount': Discount.objects.get(product=product),
        'setting_ai': setting_ai

    })


def android(request):
    setting_android = Setting_Android.objects.first()
    product = Product.objects.get(type='android')
    return render(request, 'home/android/index.html', {
        'product': product,
        'discount': Discount.objects.get(product=product),
        'setting_android': setting_android
    })


def pack(request):
    setting_pack = Setting_Pack.objects.first()
    product = Product.objects.get(type='pack')
    return render(request, 'home/pack/index.html', {
        'product': product,
        'discount': Discount.objects.get(product=product),
        'setting_pack': setting_pack
    })


def about_us(request):
    return render(request, 'home/about-us/index.html')
def term(request):
    return render(request, 'home/about-us/term.html')


def team_us(request):
    return render(request, 'home/team-us/index.html')


# Payment Views
def index(request, success=None, error=None):
    return render(request, 'home/main/index.html', {
        "products": Product.objects.all(),
        "error": error if error else None,
        "success": success if success else None
    })


def payment(request):
    if request.method == 'POST':
        is_group = False
        firstnames = request.POST.getlist('firstname[]')
        lastnames = request.POST.getlist('lastname[]')
        numbers = request.POST.getlist('number[]')
        emails = request.POST.getlist('email[]')
        coupon = request.POST.get('coupon')
        product = request.POST.get('product')

        customers_count = len(emails)

        # Validate form data
        if not firstnames or not lastnames or not numbers or not emails or not product:
            return index(request, error="Invalid parameters")

        if (len(firstnames) != customers_count) or (len(lastnames) != customers_count) or (
                len(numbers) != customers_count):
            return index(request, error="Invalid number of names or emails")

        if customers_count > 20 or customers_count == 2:
            return HttpResponse(status=400)

        if customers_count >= 3:
            is_group = True

        for i in range(customers_count):
            firstname = firstnames[i]
            lastname = lastnames[i]
            number = numbers[i]
            email = emails[i]
            validation_result = validate_data(firstname=firstname, lastname=lastname, email=email, number=number)
            if validation_result != True:
                return index(request, error=validation_result)

        try:
            product = Product.objects.get(type=product)
        except:
            return index(request, error="Invalid product")

        price = product.price * customers_count

        # Calculate price for group order
        if is_group:
            discount = Discount.objects.get(product=product)
            price -= discount.amount * customers_count

        # Process coupon code
        if coupon and not is_group:
            try:
                coupon = Coupon.objects.get(code=coupon)
                if coupon.is_expired:
                    raise Exception

                # OneTime
                if coupon.type == 'OT':
                    if coupon.owner.email != emails[0]:
                        raise Exception

                    price -= coupon.amount
                    coupon.is_expired = True
                    coupon.save()
                # Limited and Free
                elif coupon.type == 'LT' or coupon.type == 'FR':
                    price -= coupon.amount
                    if coupon.max_use == 1:
                        coupon.is_expired = True
                        coupon.save()
                    else:
                        coupon.max_use -= 1
                        coupon.save()
            except:
                return index(request, error="Invalid coupon code")
        else:
            coupon = None

        # Create transaction
        transaction = None
        try:
            default_user = User.objects.get(username="default")
        except:
            default_user = User.objects.create(username="default")

        if not coupon or coupon.type != 'FR':
            transaction_url = start_transaction(
                {
                    "user": default_user,
                    "amount": price,
                    "description": product.get_type_display(),
                    "mobile": numbers[0],
                    "email": emails[0]
                }
            )
            transaction = Transaction.objects.get(authority=transaction_url.split("/")[-1])
        else:
            transaction = Transaction.objects.create(
                user=default_user,
                status='SUCCESS',
                description=product.get_type_display(),
                amount=0,
                authority='Free'
            )

        # Create customers
        customers = []
        for i in range(customers_count):
            firstname = firstnames[i]
            lastname = lastnames[i]
            number = numbers[i]
            email = emails[i]
            try:
                customer = Customer.objects.get(firstname=firstname, lastname=lastname, number=number, email=email)
                customers.append(customer)
            except Customer.DoesNotExist:
                customer = Customer.objects.create(firstname=firstname, lastname=lastname, number=number, email=email)
                customers.append(customer)

        # Create order
        order = Order(
            buyer=customers[0],
            product=product,
            transaction=transaction
        )
        order.save()
        [order.customers.add(customer) for customer in customers]
        [customer.orders.add(order) for customer in customers]

        # Add customers to product
        product.customers.add(Customer.objects.filter(email=email).last())

        if not coupon or coupon.type != 'FR':
            return redirect(transaction_url)
        else:
            send_sms(order)
            return redirect(
                f"/winter/payment_result?type={order.product.name}&date={transaction.created_at.strftime('%H:%M:%S %d-%m-%Y')}&track_number={transaction.order_number}&is_success=True")

    return redirect("/")


def payment_result(request):
    is_success = bool(request.GET.get('is_success'))
    track_number = request.GET.get('track_number')
    date = request.GET.get('date')
    type = request.GET.get('type')

    return render(request, "home/payment_result.html", {
        'is_success': is_success,
        'track_number': track_number,
        'date': date,
        'type': type
    })


def validate_data(firstname, lastname, email, number):
    f = forms.CharField(max_length=256, required=True, validators=[
        RegexValidator('^[\u0600-\u06FF\s]+$', message="لطفا نام خود را با حروف فارسی وارد نمایید")])
    l = forms.CharField(max_length=256, required=True, validators=[
        RegexValidator('^[\u0600-\u06FF\s]+$', message="لطفا نام خانوادگی خود را با حروف فارسی وارد نمایید")])
    e = forms.EmailField(max_length=256, required=True)
    n = forms.IntegerField(required=True)

    try:
        f.clean(firstname)
        l.clean(lastname)
        e.clean(email)
        n.clean(number)
    except ValidationError as e:
        return list(e)[0]

    return True


def verify_coupon(request):
    try:
        code = request.GET['code']
        email = request.GET['email']
        coupon = Coupon.objects.get(code=code)
        if coupon.is_expired or (coupon.type == 'OT' and coupon.owner.email != email):
            raise Exception
        return HttpResponse('free' if coupon.type == 'FR' else coupon.amount, status=200)
    except:
        return HttpResponse(status=400)


def validate_payment(request):
    Authority = request.GET.get('Authority')
    Status = request.GET.get('Status')

    if not Status or not Authority:
        return index(request, error="Invalid parameters")

    try:
        transaction = verify_transaction(Status, Authority)
        order = Order.objects.get(transaction=transaction)
        is_success = True if transaction.status == "SUCCESS" else False
    except ZarinpalException:
        return index(request, error="Failed to verify the Transaction")

    order.status = transaction.status
    order.save()

    if is_success:
        send_sms(order)
    else:
        customers = []
        for customer in order.customers.all():
            if len(customer.orders.all()) == 1:
                customers.append(Customer.objects.get(id=customer.id))
        order.delete()
        [c.delete() for c in customers]

    return redirect(
        f"/winter/payment_result?type={order.product.name}&date={transaction.created_at.strftime('%H:%M:%S %d-%m-%Y')}&track_number={transaction.order_number}{'' if not is_success else '&is_success=True'}")


def send_sms(order):
    url = "http://panel.signalads.com/rest/api/v1/message/send.json"
    headers = {
        'Authorization': f'Bearer {settings.SIGNAL_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    subject_str = "تأیید ثبت‌نام در دوره‌های زمستانه | CS50x Iran" #Email Subject
    from_email = settings.EAMIL_ADDRESS
    for customer in order.customers.all():
        payload = {
            "from": settings.SIGNAL_NUMBER,
            "message": customer.firstname + " عزیز" + '\n\n'
                    f'ثبت نام شما در  دوره‌ی {order.product.get_type_display()} انجام شد. کد پیگیری شما {order.transaction.order_number} است.' + '\n\n'
                    "اطلاعات ورود به پنل کاربری را یک هفته قبل از شروع دوره برای شما ارسال خواهیم کرد." + '\n\n'
                    "سی‌اس‌فیفتی ایران" + '\n\n'
                    "cs50x.ir" + '\n\n',
            "numbers": [customer.number]
        }
        requests.post(url, headers=headers, json=payload)
        send_mail(subject_str,payload["message"],from_email,[customer.email],fail_silently=False)
