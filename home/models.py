from django.conf import settings
from django.db import models
from django_zarinpal.models import Transaction
from hashid_field import HashidAutoField
from ckeditor.fields import RichTextField
from random import randint


class Android_sessions(models.Model):
    class Meta:
        verbose_name = "جلسات اندروید"
        verbose_name_plural = "جلسات اندروید"

    titer = models.CharField("تیتر جلسه", max_length=100)
    description = models.CharField("متن کوتاه جلسه", max_length=1000)
    session_status = models.BooleanField("انتشار جلسه", default=False)
    time = models.IntegerField("زمان هر جلسه بر حسب دقیقه")
    text = RichTextField("متن توضیحات جلسه")
    question = RichTextField("متن سوال و جواب", blank=True, null=True)
    probelm_solve = models.CharField('لینک کلاس رفع اشکال', max_length=500, null=True, blank=True)
    slide_download = models.CharField('لینک دانلود اسلاید', max_length=500, null=True, blank=True)
    file_download = models.CharField('لینک دانلود فایل', max_length=500, null=True, blank=True)
    note_download = models.CharField('لینک دانلود جزوه', max_length=500, null=True, blank=True)
    session_image = models.CharField('تصویر جلسه', max_length=500, null=True, blank=True)
    first_poster = models.CharField('پوستر اولین قسمت', max_length=500, null=True, blank=True)
    first_video_link = models.CharField('لینک اولین ویدعو', max_length=300, null=True, blank=True)
    second_poster = models.CharField('پوستر دومین قسمت', max_length=500, null=True, blank=True)
    second_video_link = models.CharField('لینک دومین ویدعو', max_length=300, null=True, blank=True)


    def __str__(self):
        return self.titer


class Web_sessions(models.Model):
    class Meta:
        verbose_name = "جلسات وب"
        verbose_name_plural = "جلسات وب"

    titer = models.CharField("تیتر جلسه", max_length=100)
    description = models.CharField("متن کوتاه جلسه", max_length=1000)
    session_status = models.BooleanField("انتشار جلسه", default=False)
    time = models.IntegerField("زمان هر جلسه بر حسب دقیقه")
    text = models.CharField('لینک خلاصه متن', max_length=500, null=True, blank=True)
    question = RichTextField("متن سوال و جواب", blank=True, null=True)
    probelm_solve = models.CharField('لینک کلاس رفع اشکال', max_length=500, null=True, blank=True)
    slide_download = models.CharField('لینک دانلود اسلاید', max_length=500, null=True, blank=True)
    file_download = models.CharField('لینک دانلود فایل', max_length=500, null=True, blank=True)
    note_download = models.CharField('لینک دانلود جزوه', max_length=500, null=True, blank=True)
    session_image = models.CharField('تصویر جلسه', max_length=500, null=True)
    first_poster = models.CharField('پوستر اولین قسمت', max_length=500, null=True, blank=True)
    first_video_link = models.CharField('لینک اولین ویدعو', max_length=300, null=True, blank=True)
    second_poster = models.CharField('پوستر دومین قسمت', max_length=500, null=True, blank=True)
    second_video_link = models.CharField('لینک دومین ویدعو', max_length=300, null=True, blank=True)

    def __str__(self):
        return self.titer


class Ai_sessions(models.Model):
    class Meta:
        verbose_name = "جلسات هوش مصنوعی"
        verbose_name_plural = "جلسات هوش مصنوعی"

    titer = models.CharField("تیتر جلسه", max_length=100)
    description = models.CharField("متن کوتاه جلسه", max_length=1000)
    session_status = models.BooleanField("انتشار جلسه", default=False)
    time = models.IntegerField("زمان هر جلسه بر حسب دقیقه")
    text = models.CharField('لینک خلاصه متن', max_length=500, null=True, blank=True)
    question = RichTextField("متن سوال و جواب", blank=True, null=True)
    quiz = RichTextField("متن کوئیز", blank=True, null=True)
    probelm_solve = models.CharField('لینک کلاس رفع اشکال', max_length=500, null=True, blank=True)
    slide_download = models.CharField('لینک دانلود اسلاید', max_length=500, null=True, blank=True)
    file_download = models.CharField('لینک دانلود فایل', max_length=500, null=True, blank=True)
    note_download = models.CharField('لینک دانلود جزوه', max_length=500, null=True, blank=True)
    session_image = models.CharField('تصویر جلسه', max_length=500, null=True)
    first_poster = models.CharField('پوستر اولین قسمت', max_length=500, null=True, blank=True)
    first_video_link = models.CharField('لینک اولین ویدعو', max_length=300, null=True, blank=True)
    second_poster = models.CharField('پوستر دومین قسمت', max_length=500, null=True, blank=True)
    second_video_link = models.CharField('لینک دومین ویدعو', max_length=300, null=True, blank=True)

    def __str__(self):
        return self.titer




class Customer(models.Model):
    firstname = models.CharField(max_length=256, blank=False)
    lastname = models.CharField(max_length=256, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    number = models.CharField(max_length=128, blank=False)
    orders = models.ManyToManyField("Order", blank=True, related_name="orders")

    def __str__(self):
        return self.firstname

class Product(models.Model):
    TYPE_CHOICES = (
        ('android', 'Android'),
        ('ai', 'Artificial Intelligence'),
        ('web', 'Web'),
        ('pack', 'Pack'),
        ('android-ins', 'Android Ins'),
        ('ai-ins', 'Artificial Intelligence Ins'),
        ('web-ins', 'Web Ins'),
        ('pack-ins', 'Pack Ins')
    )
    name = models.CharField(max_length=256, blank=False)
    price = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, blank=False)
    customers = models.ManyToManyField(Customer, blank=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    TRANSACTION_STATUS_CHOICES = (
        ("PENDING", "Transaction has just started"),
        ("FAILED", "Transaction has failed"),
        ("SUCCESS", "Transaction has successfully done"),
    )
    track_number = HashidAutoField(allow_int_lookup=True, primary_key=True, salt=getattr(settings, "HASHID_FIELD_SALT", None))
    buyer = models.ForeignKey(Customer, blank=False, on_delete=models.DO_NOTHING)
    customers = models.ManyToManyField(Customer, blank=True, related_name="customers")
    product = models.ForeignKey(Product, blank=False, on_delete=models.DO_NOTHING)
    transaction = models.ForeignKey(Transaction, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=TRANSACTION_STATUS_CHOICES, default="PENDING")
    cuopon = models.ForeignKey('Coupon', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.track_number)

class Coupon(models.Model):
    TYPE_CHOICES = (
        ('OT', 'OneTime'),
        ('LT', 'Limited'),
        ('FR', 'Free')
    )
    code = models.CharField(max_length=128, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, blank=False)
    owner = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    max_use = models.IntegerField(null=True, blank=False, default=0)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class Discount(models.Model):
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.product.name

# Landing AI
class Setting_AI(models.Model):
    course_title = models.CharField(verbose_name='تیتر دوره', max_length=1000, blank=True, default=False)
    course_description = models.CharField(verbose_name='توضیحات زیر تیتر دوره', max_length=1000, blank=True, default=False)
    left_button = models.CharField(verbose_name='دکمه سمت چپ', max_length=256, blank=True, default=False)
    right_button = models.CharField(verbose_name='دکمه سمت راست', max_length=256, blank=True, default=False)
    course_feature_title1 = models.CharField(verbose_name='تیتر ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_description1 = models.CharField(verbose_name='توضیحات ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_title2 = models.CharField(verbose_name='تیتر ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_description2 = models.CharField(verbose_name='توضیحات ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_title3 = models.CharField(verbose_name='تیتر ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_description3 = models.CharField(verbose_name='توضیحات ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_title4 = models.CharField(verbose_name='تیتر ویژگی چهارم', max_length=256, blank=True, default=False)
    course_feature_description4 = models.CharField(verbose_name='توضیحات ویژگی چهارم', max_length=256, blank=True, default=False)
    david_video_title = models.CharField(verbose_name='تیتر زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description1 = models.CharField(verbose_name='توضیحات خط اول زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description2 = models.CharField(verbose_name='توضیحات خط دوم زیر ویدئو david', max_length=256, blank=True, default=False)
    skills_title = models.CharField(verbose_name='تیتر مهارت ها', max_length=256, blank=True, default=False)
    skills_title1 = models.CharField(verbose_name='تیتر مهارت اول', max_length=256, blank=True, default=False)
    skill_description1 = models.CharField(verbose_name='توضیحات خط اول مهارت اول', max_length=256, blank=True, default=False)
    skill_description1_1 = models.CharField(verbose_name='توضیحات خط دوم مهارت اول', max_length=256, blank=True, default=False)
    skills_title2 = models.CharField(verbose_name='تیتر مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2 = models.CharField(verbose_name='توضیحات خط اول مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2_2 = models.CharField(verbose_name='توضیحات خط دوم مهارت دوم', max_length=256, blank=True, default=False)
    skills_title3 = models.CharField(verbose_name='تیتر مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3 = models.CharField(verbose_name='توضیحات خط اول مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3_3 = models.CharField(verbose_name='توضیحات خط دوم مهارت سوم', max_length=256, blank=True, default=False)
    skills_title4 = models.CharField(verbose_name='تیتر مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4 = models.CharField(verbose_name='توضیحات خط اول مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4_4 = models.CharField(verbose_name='توضیحات خط دوم مهارت چهارم', max_length=256, blank=True, default=False)
    course_topic = models.CharField(verbose_name='تیتر سرفصل دوره', max_length=256, blank=True, default=False)
    course_skill_topic = models.CharField(verbose_name='عنوان دوره', max_length=256, blank=True, default=False)
    teacher_name = models.CharField(verbose_name='اسم مدرس', max_length=256, blank=True, default=False)
    teacher_description = models.CharField(verbose_name='توضیحات مدرس', max_length=1000, blank=True, default=False)
    suitable_for_title = models.CharField(verbose_name='تیتر دوره مناسب چه افرادی است', max_length=256, blank=True, default=False)
    suitable_for_title1 = models.CharField(verbose_name='توضیح اول', max_length=256, blank=True, default=False)
    suitable_for_title2 = models.CharField(verbose_name='توضیح دوم', max_length=256, blank=True, default=False)
    suitable_for_title3 = models.CharField(verbose_name='توضیح سوم', max_length=256, blank=True, default=False)
    suitable_for_title4 = models.CharField(verbose_name='توضیح چهارم', max_length=256, blank=True, default=False)
    title_of_document = models.CharField(verbose_name='تیتر مدرک هاروارد', max_length=256, blank=True, default=False)
    david_video_title_under_register = models.CharField(verbose_name='تیتر روبه روی ویدئو david', max_length=256, blank=True, default=False)
    david_video_description_under_register = models.CharField(verbose_name='توضیحات روبه روی ویدئو david', max_length=256, blank=True, default=False)
    who_are_we_title = models.CharField(verbose_name='تیتر ما کی هستیم؟', max_length=256, blank=True, default=False)
    who_are_we_description1 = models.CharField(verbose_name='توضیحات خط اول ما کی هستیم', max_length=256, blank=True, default=False)
    who_are_we_description2 = models.CharField(verbose_name='توضیحات خط دوم ما کی هستیم', max_length=256, blank=True, default=False)
    right_course_title = models.CharField(verbose_name='تیتر دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_description = models.CharField(verbose_name='توضیحات دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_price = models.CharField(verbose_name='قیمت دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    left_course_title = models.CharField(verbose_name='تیتر دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_description = models.CharField(verbose_name='توضیحات دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_price = models.CharField(verbose_name='قیمت دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)

    class Meta:
        verbose_name = 'تنظیمات لندینگ هوش مصنوعی'
        verbose_name_plural = 'مدیریت تنظیمات لندینگ هوش مصنوعی'



# Landing Android
class Setting_Android(models.Model):
    course_title = models.CharField(verbose_name='تیتر دوره', max_length=1000, blank=True, default=False)
    course_description = models.CharField(verbose_name='توضیحات زیر تیتر دوره', max_length=1000, blank=True, default=False)
    left_button = models.CharField(verbose_name='دکمه سمت چپ', max_length=256, blank=True, default=False)
    right_button = models.CharField(verbose_name='دکمه سمت راست', max_length=256, blank=True, default=False)
    course_feature_title1 = models.CharField(verbose_name='تیتر ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_description1 = models.CharField(verbose_name='توضیحات ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_title2 = models.CharField(verbose_name='تیتر ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_description2 = models.CharField(verbose_name='توضیحات ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_title3 = models.CharField(verbose_name='تیتر ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_description3 = models.CharField(verbose_name='توضیحات ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_title4 = models.CharField(verbose_name='تیتر ویژگی چهارم', max_length=256, blank=True, default=False)
    course_feature_description4 = models.CharField(verbose_name='توضیحات ویژگی چهارم', max_length=256, blank=True, default=False)
    david_video_title = models.CharField(verbose_name='تیتر زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description1 = models.CharField(verbose_name='توضیحات خط اول زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description2 = models.CharField(verbose_name='توضیحات خط دوم زیر ویدئو david', max_length=256, blank=True, default=False)
    skills_title = models.CharField(verbose_name='تیتر مهارت ها', max_length=256, blank=True, default=False)
    skills_title1 = models.CharField(verbose_name='تیتر مهارت اول', max_length=256, blank=True, default=False)
    skill_description1 = models.CharField(verbose_name='توضیحات خط اول مهارت اول', max_length=256, blank=True, default=False)
    skill_description1_1 = models.CharField(verbose_name='توضیحات خط دوم مهارت اول', max_length=256, blank=True, default=False)
    skills_title2 = models.CharField(verbose_name='تیتر مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2 = models.CharField(verbose_name='توضیحات خط اول مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2_2 = models.CharField(verbose_name='توضیحات خط دوم مهارت دوم', max_length=256, blank=True, default=False)
    skills_title3 = models.CharField(verbose_name='تیتر مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3 = models.CharField(verbose_name='توضیحات خط اول مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3_3 = models.CharField(verbose_name='توضیحات خط دوم مهارت سوم', max_length=256, blank=True, default=False)
    skills_title4 = models.CharField(verbose_name='تیتر مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4 = models.CharField(verbose_name='توضیحات خط اول مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4_4 = models.CharField(verbose_name='توضیحات خط دوم مهارت چهارم', max_length=256, blank=True, default=False)
    course_topic = models.CharField(verbose_name='تیتر سرفصل دوره', max_length=256, blank=True, default=False)
    course_skill_topic = models.CharField(verbose_name='عنوان دوره', max_length=256, blank=True, default=False)
    teacher_name = models.CharField(verbose_name='اسم مدرس', max_length=256, blank=True, default=False)
    teacher_description = models.CharField(verbose_name='توضیحات مدرس', max_length=1000, blank=True, default=False)
    suitable_for_title = models.CharField(verbose_name='تیتر دوره مناسب چه افرادی است', max_length=256, blank=True, default=False)
    suitable_for_title1 = models.CharField(verbose_name='توضیح اول', max_length=256, blank=True, default=False)
    suitable_for_title2 = models.CharField(verbose_name='توضیح دوم', max_length=256, blank=True, default=False)
    suitable_for_title3 = models.CharField(verbose_name='توضیح سوم', max_length=256, blank=True, default=False)
    suitable_for_title4 = models.CharField(verbose_name='توضیح چهارم', max_length=256, blank=True, default=False)
    title_of_document = models.CharField(verbose_name='تیتر مدرک هاروارد', max_length=256, blank=True, default=False)
    david_video_title_under_register = models.CharField(verbose_name='تیتر روبه روی ویدئو david', max_length=256, blank=True, default=False)
    david_video_description_under_register = models.CharField(verbose_name='توضیحات روبه روی ویدئو david', max_length=256, blank=True, default=False)
    who_are_we_title = models.CharField(verbose_name='تیتر ما کی هستیم؟', max_length=256, blank=True, default=False)
    who_are_we_description1 = models.CharField(verbose_name='توضیحات خط اول ما کی هستیم', max_length=256, blank=True, default=False)
    who_are_we_description2 = models.CharField(verbose_name='توضیحات خط دوم ما کی هستیم', max_length=256, blank=True, default=False)
    right_course_title = models.CharField(verbose_name='تیتر دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_description = models.CharField(verbose_name='توضیحات دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_price = models.CharField(verbose_name='قیمت دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    left_course_title = models.CharField(verbose_name='تیتر دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_description = models.CharField(verbose_name='توضیحات دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_price = models.CharField(verbose_name='قیمت دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)

    class Meta:
        verbose_name = 'تنظیمات لندینگ اندروید'
        verbose_name_plural = 'مدیریت تنظیمات لندینگ اندروید'

# Landing Web
class Setting_Web(models.Model):
    course_title = models.CharField(verbose_name='تیتر دوره', max_length=1000, blank=True, default=False)
    course_description = models.CharField(verbose_name='توضیحات زیر تیتر دوره', max_length=1000, blank=True, default=False)
    left_button = models.CharField(verbose_name='دکمه سمت چپ', max_length=256, blank=True, default=False)
    right_button = models.CharField(verbose_name='دکمه سمت راست', max_length=256, blank=True, default=False)
    course_feature_title1 = models.CharField(verbose_name='تیتر ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_description1 = models.CharField(verbose_name='توضیحات ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_title2 = models.CharField(verbose_name='تیتر ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_description2 = models.CharField(verbose_name='توضیحات ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_title3 = models.CharField(verbose_name='تیتر ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_description3 = models.CharField(verbose_name='توضیحات ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_title4 = models.CharField(verbose_name='تیتر ویژگی چهارم', max_length=256, blank=True, default=False)
    course_feature_description4 = models.CharField(verbose_name='توضیحات ویژگی چهارم', max_length=256, blank=True, default=False)
    david_video_title = models.CharField(verbose_name='تیتر زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description1 = models.CharField(verbose_name='توضیحات خط اول زیر ویدئو david', max_length=256, blank=True, default=False)
    david_video_description2 = models.CharField(verbose_name='توضیحات خط دوم زیر ویدئو david', max_length=256, blank=True, default=False)
    skills_title = models.CharField(verbose_name='تیتر مهارت ها', max_length=256, blank=True, default=False)
    skills_title1 = models.CharField(verbose_name='تیتر مهارت اول', max_length=256, blank=True, default=False)
    skill_description1 = models.CharField(verbose_name='توضیحات خط اول مهارت اول', max_length=256, blank=True, default=False)
    skill_description1_1 = models.CharField(verbose_name='توضیحات خط دوم مهارت اول', max_length=256, blank=True, default=False)
    skills_title2 = models.CharField(verbose_name='تیتر مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2 = models.CharField(verbose_name='توضیحات خط اول مهارت دوم', max_length=256, blank=True, default=False)
    skill_description2_2 = models.CharField(verbose_name='توضیحات خط دوم مهارت دوم', max_length=256, blank=True, default=False)
    skills_title3 = models.CharField(verbose_name='تیتر مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3 = models.CharField(verbose_name='توضیحات خط اول مهارت سوم', max_length=256, blank=True, default=False)
    skill_description3_3 = models.CharField(verbose_name='توضیحات خط دوم مهارت سوم', max_length=256, blank=True, default=False)
    skills_title4 = models.CharField(verbose_name='تیتر مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4 = models.CharField(verbose_name='توضیحات خط اول مهارت چهارم', max_length=256, blank=True, default=False)
    skill_description4_4 = models.CharField(verbose_name='توضیحات خط دوم مهارت چهارم', max_length=256, blank=True, default=False)
    course_topic = models.CharField(verbose_name='تیتر سرفصل دوره', max_length=256, blank=True, default=False)
    course_skill_topic = models.CharField(verbose_name='عنوان دوره', max_length=256, blank=True, default=False)
    teacher_name = models.CharField(verbose_name='اسم مدرس', max_length=256, blank=True, default=False)
    teacher_description = models.CharField(verbose_name='توضیحات مدرس', max_length=1000, blank=True, default=False)
    suitable_for_title = models.CharField(verbose_name='تیتر دوره مناسب چه افرادی است', max_length=256, blank=True, default=False)
    suitable_for_title1 = models.CharField(verbose_name='توضیح اول', max_length=256, blank=True, default=False)
    suitable_for_title2 = models.CharField(verbose_name='توضیح دوم', max_length=256, blank=True, default=False)
    suitable_for_title3 = models.CharField(verbose_name='توضیح سوم', max_length=256, blank=True, default=False)
    suitable_for_title4 = models.CharField(verbose_name='توضیح چهارم', max_length=256, blank=True, default=False)
    title_of_document = models.CharField(verbose_name='تیتر مدرک هاروارد', max_length=256, blank=True, default=False)
    david_video_title_under_register = models.CharField(verbose_name='تیتر روبه روی ویدئو david', max_length=256, blank=True, default=False)
    david_video_description_under_register = models.CharField(verbose_name='توضیحات روبه روی ویدئو david', max_length=256, blank=True, default=False)
    who_are_we_title = models.CharField(verbose_name='تیتر ما کی هستیم؟', max_length=256, blank=True, default=False)
    who_are_we_description1 = models.CharField(verbose_name='توضیحات خط اول ما کی هستیم', max_length=256, blank=True, default=False)
    who_are_we_description2 = models.CharField(verbose_name='توضیحات خط دوم ما کی هستیم', max_length=256, blank=True, default=False)
    right_course_title = models.CharField(verbose_name='تیتر دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_description = models.CharField(verbose_name='توضیحات دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    right_course_price = models.CharField(verbose_name='قیمت دوره سمت راست انتهای سایت', max_length=256, blank=True, default=False)
    left_course_title = models.CharField(verbose_name='تیتر دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_description = models.CharField(verbose_name='توضیحات دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)
    left_course_price = models.CharField(verbose_name='قیمت دوره سمت چپ انتهای سایت', max_length=256, blank=True, default=False)

    class Meta:
        verbose_name = 'تنظیمات لندینگ وب'
        verbose_name_plural = 'مدیریت تنظیمات لندینگ وب'

# Landing Pack
class Setting_Pack(models.Model):
    course_title = models.CharField(verbose_name='تیتر دوره', max_length=1000, blank=True, default=False)
    course_description = models.CharField(verbose_name='توضیحات زیر تیتر دوره', max_length=1000, blank=True, default=False)
    left_button = models.CharField(verbose_name='دکمه سمت چپ', max_length=256, blank=True, default=False)
    right_button = models.CharField(verbose_name='دکمه سمت راست', max_length=256, blank=True, default=False)
    title_of_document = models.CharField(verbose_name='تیتر مدرک هاروارد', max_length=256, blank=True, default=False)
    david_video_title_under_register = models.CharField(verbose_name='تیتر روبه روی ویدئو david', max_length=256, blank=True, default=False)
    david_video_description_under_register = models.CharField(verbose_name='توضیحات روبه روی ویدئو david', max_length=256, blank=True, default=False)
    course_feature_title1 = models.CharField(verbose_name='تیتر ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_description1 = models.CharField(verbose_name='توضیحات ویژگی اول', max_length=256, blank=True, default=False)
    course_feature_title2 = models.CharField(verbose_name='تیتر ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_description2 = models.CharField(verbose_name='توضیحات ویژگی دوم', max_length=256, blank=True, default=False)
    course_feature_title3 = models.CharField(verbose_name='تیتر ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_description3 = models.CharField(verbose_name='توضیحات ویژگی سوم', max_length=256, blank=True, default=False)
    course_feature_title4 = models.CharField(verbose_name='تیتر ویژگی چهارم', max_length=256, blank=True, default=False)
    course_feature_description4 = models.CharField(verbose_name='توضیحات ویژگی چهارم', max_length=256, blank=True, default=False)
    course_topic = models.CharField(verbose_name='تیتر سرفصل دوره', max_length=256, blank=True, default=False)
    course_under_description1 = models.CharField(verbose_name='توضیحات زیر سر فصل دوره خط اول', max_length=256, blank=True, default=False)
    course_under_description2 = models.CharField(verbose_name='توضیحات زیر سر فصل دوره خط دوم', max_length=256, blank=True, default=False)
    course_web_title = models.CharField(verbose_name='تیتر دوره وب زیر سر فصل', max_length=256, blank=True, default=False)
    course_web_description1 = models.CharField(verbose_name='توضیح خط اول سرفصل وب', max_length=256, blank=True, default=False)
    course_web_description2 = models.CharField(verbose_name='توضیح خط دوم سر فصل وب', max_length=256, blank=True, default=False)
    course_web_description3 = models.CharField(verbose_name='توضیح خط سوم سرفصل وب', max_length=256, blank=True, default=False)
    course_web_description4 = models.CharField(verbose_name='توضیح خط چهارم سرفصل وب', max_length=256, blank=True, default=False)
    course_android_title = models.CharField(verbose_name='تیتر دوره اندروید زیر سرفصل', max_length=256, blank=True, default=False)
    course_android_description1 = models.CharField(verbose_name='توضیح خط اول سرفصل اندروید', max_length=256, blank=True, default=False)
    course_android_description2 = models.CharField(verbose_name='توضیح خط دوم سر فصل اندروید', max_length=256, blank=True, default=False)
    course_android_description3 = models.CharField(verbose_name='توضیح خط سوم سرفصل اندروید', max_length=256, blank=True, default=False)
    course_android_description4 = models.CharField(verbose_name='توضیح خط چهارم سرفصل اندروید', max_length=256, blank=True, default=False)
    course_ai_title = models.CharField(verbose_name='تیتر دوره هوش مصنوعی زیر سرفصل', max_length=256, blank=True, default=False)
    course_ai_description1 = models.CharField(verbose_name='توضیح خط اول سرفصل هوش مصنوعی', max_length=256, blank=True, default=False)
    course_ai_description2 = models.CharField(verbose_name='توضیح خط دوم سر فصل هوش مصنوعی', max_length=256, blank=True, default=False)
    course_ai_description3 = models.CharField(verbose_name='توضیح خط سوم سرفصل هوش مصنوعی', max_length=256, blank=True, default=False)
    course_ai_description4 = models.CharField(verbose_name='توضیح خط چهارم سرفصل هوش مصنوعی', max_length=256, blank=True, default=False)
    first_teacher_name = models.CharField(verbose_name='نام اولین مدرس', max_length=256, blank=True, default=False)
    first_teacher_description = models.CharField(verbose_name='توضیحات زیر نام اولین مدرس', max_length=256, blank=True, default=False)
    first_teacher_button = models.CharField(verbose_name='متن داخل دکمه اولین مدرس', max_length=256, blank=True, default=False)
    second_teacher_name = models.CharField(verbose_name='نام دومین مدرس', max_length=256, blank=True, default=False)
    second_teacher_description = models.CharField(verbose_name='توضیحات زیر نام دومین مدرس', max_length=256, blank=True, default=False)
    second_teacher_button = models.CharField(verbose_name='متن داخل دکمه دومین مدرس', max_length=256, blank=True, default=False)
    third_teacher_name = models.CharField(verbose_name='نام سومین مدرس', max_length=256, blank=True, default=False)
    third_teacher_description = models.CharField(verbose_name='توضیحات زیر نام سومین مدرس', max_length=256, blank=True, default=False)
    third_teacher_button = models.CharField(verbose_name='متن داخل دکمه سومین مدرس', max_length=256, blank=True, default=False)


    class Meta:
        verbose_name = 'تنظیمات لندینگ پکیج'
        verbose_name_plural = 'مدیریت تنظیمات لندینگ پکیج'
