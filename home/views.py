from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django_zarinpal.services import start_transaction, verify_transaction
from django.core.mail import send_mail
from django_zarinpal.exceptions import ZarinpalException
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .forms import UpdateAccount
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
from django import forms
from .models import *
from account.models import User
import requests
import json


# Pages
@login_required
def web_class(request):
    web_sessions = Web_sessions.objects.all()
    context = {
        'web_sessions': web_sessions
    }
    if request.user.complete_profile:
        if request.user.web:
            return render(request, 'home/web/web.html', context)
    else:
        return HttpResponseRedirect(reverse('profile_edite'))


@login_required
def ai_class(request):
    ai_sessions = Ai_sessions.objects.all()
    context = {
        'ai_sessions': ai_sessions
    }
    if request.user.complete_profile:
        if request.user.ai:
            return render(request, 'home/ai/ai.html', context)
    else:
        return HttpResponseRedirect(reverse('profile_edite'))


@login_required
def android_class(request):
    android_sessions = Android_sessions.objects.all()
    context = {
        'android_sessions': android_sessions
    }
    if request.user.complete_profile:
        if request.user.android:
            return render(request, 'home/android/android.html', context)
    else:
        return HttpResponseRedirect(reverse('profile_edite'))


@login_required
def android_class_sessions(request, session_id):
    session = get_object_or_404(Android_sessions, pk=session_id)
    context = {
        'session': session
    }
    t = session.session_status
    if t:
        if request.user.complete_profile:
            if request.user.android:
                return render(request, 'home/android/details.html', context)
    else:
        return HttpResponseRedirect(reverse("ai_class"))


@login_required
def ai_class_sessions(request, session_id):
    session = get_object_or_404(Ai_sessions, pk=session_id)
    context = {
        'session': session
    }
    t = session.session_status
    if t:
        if request.user.complete_profile:
            if request.user.ai:
                return render(request, 'home/ai/details.html', context)
    else:
        return HttpResponseRedirect(reverse("ai_class"))


@login_required
def web_class_sessions(request, session_id):
    session = get_object_or_404(Web_sessions, pk=session_id)
    context = {
        'session': session
    }
    t = session.session_status
    if t:
        if request.user.complete_profile:
            if request.user.web:
                return render(request, 'home/web/details.html', context)
    else:
        return HttpResponseRedirect(reverse("web_class"))


# # Main
# def index(request):
#     return render(request, 'home/main/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Successfully login
            login(request, user)
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return HttpResponseRedirect(reverse("dashbord"))
        else:
            context = {
                "email": email,
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("dashbord"))

        context = {}
    return render(request, "home/signin/index.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("dashbord"))


@login_required
def dashbord(request):
    return render(request, 'home/profile/dashbord.html')


@login_required
def ai_class_sessions_description(request, session_id):
    session = get_object_or_404(Ai_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.ai:
            if t:
                return render(request, "home/ai/ai_class_sessions_description.html", context)
            else:
                return HttpResponseRedirect(reverse('ai_class'))
    else:
        return HttpResponseRedirect(reverse('ai_class'))


@login_required
def ai_class_sessions_question(request, session_id):
    session = get_object_or_404(Ai_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.ai:
            if t:
                return render(request, "home/ai/ai_class_sessions_question.html", context)
            else:
                return HttpResponseRedirect(reverse('ai_class'))
    else:
        return HttpResponseRedirect(reverse('ai_class'))


@login_required
def web_class_sessions_description(request, session_id):
    session = get_object_or_404(Web_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.web:
            if t:
                return render(request, "home/web/web_class_sessions_description.html", context)
            else:
                return HttpResponseRedirect(reverse('web_class'))
    else:
        return HttpResponseRedirect(reverse('web_class'))


@login_required
def web_class_sessions_question(request, session_id):
    session = get_object_or_404(Web_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.web:
            if t:
                return render(request, "home/web/web_class_sessions_question.html", context)
            else:
                return HttpResponseRedirect(reverse('web_class'))
    else:
        return HttpResponseRedirect(reverse('web_class'))


@login_required
def android_class_sessions_description(request, session_id):
    session = get_object_or_404(Android_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.android:
            if t:
                return render(request, "home/android/android_class_sessions_description.html", context)
            else:
                return HttpResponseRedirect(reverse('android_class'))
    else:
        return HttpResponseRedirect(reverse('android_class'))


@login_required
def android_class_sessions_question(request, session_id):
    session = get_object_or_404(Android_sessions, pk=session_id)
    t = session.session_status
    context = {
        'session': session
    }
    if request.user.complete_profile:
        if request.user.android:
            if t:
                return render(request, "home/android/android_class_sessions_question.html", context)
            else:
                return HttpResponseRedirect(reverse('android_class'))
    else:
        return HttpResponseRedirect(reverse('android_class'))


def profile(request):
    return render(request, 'home/profile/profile.html')


@login_required
def profile_edite(request):
    form = UpdateAccount(instance=request.user)
    if request.method == 'POST':
        form = UpdateAccount(request.POST, instance=request.user)
        if form.is_valid():
            request.user.complete_profile = True
            form.save()
            return HttpResponseRedirect(reverse('dashbord'))
    return render(request, "home/profile/profile_edite.html", {'form': form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "home/profile/change_password.html", {"form": form})





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

        if customers_count > 20:
            return HttpResponse(status=400)

        if customers_count >= 2:
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
        if coupon:
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
            default_user = User.objects.get(email="default")
        except:
            default_user = User.objects.create(email="default")

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

    subject_str = "تأیید ثبت‌نام در دوره‌های زمستانه | CS50x Iran"  # Email Subject
    from_email = settings.EAMIL_ADDRESS
    for customer in order.customers.all():
        payload = {
            "from": settings.SIGNAL_NUMBER,
            "message": customer.firstname + " عزیز" + '\n\n'
                    f'ثبت نام شما در  دوره‌ی {order.product.get_type_display()} انجام شد. کد پیگیری شما {order.transaction.order_number} است.' + '\n\n'
                    "اطلاعات ورود به پنل کاربری به زودی برای شما ارسال خواهد شد." + '\n\n'
                    "سی‌اس‌فیفتی ایران" + '\n\n'
                    "cs50x.ir" + '\n\n',
            "numbers": [customer.number]
        }
        requests.post(url, headers=headers, json=payload)
        send_mail(subject_str, payload["message"], from_email, [customer.email], fail_silently=False)
        
        
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': 'cs50x.ir',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'hello@cs50x.ir', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={
        "password_reset_form": password_reset_form
    })
        
