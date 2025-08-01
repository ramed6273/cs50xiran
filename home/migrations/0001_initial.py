# Generated by Django 3.2.8 on 2022-01-01 11:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_zarinpal', '0002_auto_20211204_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ai_sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titer', models.CharField(max_length=100, verbose_name='تیتر جلسه')),
                ('description', models.CharField(max_length=1000, verbose_name='متن کوتاه جلسه')),
                ('session_status', models.BooleanField(default=False, verbose_name='انتشار جلسه')),
                ('time', models.IntegerField(verbose_name='زمان هر جلسه بر حسب دقیقه')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک خلاصه متن')),
                ('question', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن سوال و جواب')),
                ('quiz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن کوئیز')),
                ('probelm_solve', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک کلاس رفع اشکال')),
                ('slide_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود اسلاید')),
                ('file_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود فایل')),
                ('note_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود جزوه')),
                ('session_image', models.CharField(max_length=500, null=True, verbose_name='تصویر جلسه')),
                ('first_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر اولین قسمت')),
                ('first_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک اولین ویدعو')),
                ('second_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر دومین قسمت')),
                ('second_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک دومین ویدعو')),
            ],
            options={
                'verbose_name': 'جلسات هوش مصنوعی',
                'verbose_name_plural': 'جلسات هوش مصنوعی',
            },
        ),
        migrations.CreateModel(
            name='Android_sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titer', models.CharField(max_length=100, verbose_name='تیتر جلسه')),
                ('description', models.CharField(max_length=1000, verbose_name='متن کوتاه جلسه')),
                ('session_status', models.BooleanField(default=False, verbose_name='انتشار جلسه')),
                ('time', models.IntegerField(verbose_name='زمان هر جلسه بر حسب دقیقه')),
                ('text', ckeditor.fields.RichTextField(verbose_name='متن توضیحات جلسه')),
                ('question', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن سوال و جواب')),
                ('probelm_solve', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک کلاس رفع اشکال')),
                ('slide_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود اسلاید')),
                ('file_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود فایل')),
                ('note_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود جزوه')),
                ('session_image', models.CharField(blank=True, max_length=500, null=True, verbose_name='تصویر جلسه')),
                ('first_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر اولین قسمت')),
                ('first_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک اولین ویدعو')),
                ('second_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر دومین قسمت')),
                ('second_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک دومین ویدعو')),
            ],
            options={
                'verbose_name': 'جلسات اندروید',
                'verbose_name_plural': 'جلسات اندروید',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128)),
                ('amount', models.IntegerField()),
                ('type', models.CharField(choices=[('OT', 'OneTime'), ('LT', 'Limited'), ('FR', 'Free')], max_length=64)),
                ('max_use', models.IntegerField(default=0, null=True)),
                ('is_expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('number', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Setting_AI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(blank=True, default=False, max_length=1000, verbose_name='تیتر دوره')),
                ('course_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات زیر تیتر دوره')),
                ('left_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت چپ')),
                ('right_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت راست')),
                ('course_feature_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی اول')),
                ('course_feature_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی اول')),
                ('course_feature_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی دوم')),
                ('course_feature_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی دوم')),
                ('course_feature_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی سوم')),
                ('course_feature_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی سوم')),
                ('course_feature_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی چهارم')),
                ('course_feature_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی چهارم')),
                ('david_video_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر زیر ویدئو david')),
                ('david_video_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول زیر ویدئو david')),
                ('david_video_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم زیر ویدئو david')),
                ('skills_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت ها')),
                ('skills_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت اول')),
                ('skill_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت اول')),
                ('skill_description1_1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت اول')),
                ('skills_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت دوم')),
                ('skill_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت دوم')),
                ('skill_description2_2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت دوم')),
                ('skills_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت سوم')),
                ('skill_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت سوم')),
                ('skill_description3_3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت سوم')),
                ('skills_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت چهارم')),
                ('skill_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت چهارم')),
                ('skill_description4_4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت چهارم')),
                ('course_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر سرفصل دوره')),
                ('course_skill_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='عنوان دوره')),
                ('teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='اسم مدرس')),
                ('teacher_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات مدرس')),
                ('suitable_for_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره مناسب چه افرادی است')),
                ('suitable_for_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح اول')),
                ('suitable_for_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح دوم')),
                ('suitable_for_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح سوم')),
                ('suitable_for_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح چهارم')),
                ('title_of_document', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مدرک هاروارد')),
                ('david_video_title_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر روبه روی ویدئو david')),
                ('david_video_description_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات روبه روی ویدئو david')),
                ('who_are_we_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ما کی هستیم؟')),
                ('who_are_we_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول ما کی هستیم')),
                ('who_are_we_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم ما کی هستیم')),
                ('right_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت راست انتهای سایت')),
                ('right_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت راست انتهای سایت')),
                ('right_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت راست انتهای سایت')),
                ('left_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت چپ انتهای سایت')),
                ('left_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت چپ انتهای سایت')),
                ('left_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت چپ انتهای سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات لندینگ هوش مصنوعی',
                'verbose_name_plural': 'مدیریت تنظیمات لندینگ هوش مصنوعی',
            },
        ),
        migrations.CreateModel(
            name='Setting_Android',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(blank=True, default=False, max_length=1000, verbose_name='تیتر دوره')),
                ('course_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات زیر تیتر دوره')),
                ('left_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت چپ')),
                ('right_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت راست')),
                ('course_feature_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی اول')),
                ('course_feature_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی اول')),
                ('course_feature_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی دوم')),
                ('course_feature_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی دوم')),
                ('course_feature_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی سوم')),
                ('course_feature_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی سوم')),
                ('course_feature_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی چهارم')),
                ('course_feature_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی چهارم')),
                ('david_video_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر زیر ویدئو david')),
                ('david_video_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول زیر ویدئو david')),
                ('david_video_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم زیر ویدئو david')),
                ('skills_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت ها')),
                ('skills_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت اول')),
                ('skill_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت اول')),
                ('skill_description1_1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت اول')),
                ('skills_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت دوم')),
                ('skill_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت دوم')),
                ('skill_description2_2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت دوم')),
                ('skills_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت سوم')),
                ('skill_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت سوم')),
                ('skill_description3_3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت سوم')),
                ('skills_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت چهارم')),
                ('skill_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت چهارم')),
                ('skill_description4_4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت چهارم')),
                ('course_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر سرفصل دوره')),
                ('course_skill_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='عنوان دوره')),
                ('teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='اسم مدرس')),
                ('teacher_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات مدرس')),
                ('suitable_for_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره مناسب چه افرادی است')),
                ('suitable_for_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح اول')),
                ('suitable_for_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح دوم')),
                ('suitable_for_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح سوم')),
                ('suitable_for_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح چهارم')),
                ('title_of_document', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مدرک هاروارد')),
                ('david_video_title_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر روبه روی ویدئو david')),
                ('david_video_description_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات روبه روی ویدئو david')),
                ('who_are_we_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ما کی هستیم؟')),
                ('who_are_we_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول ما کی هستیم')),
                ('who_are_we_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم ما کی هستیم')),
                ('right_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت راست انتهای سایت')),
                ('right_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت راست انتهای سایت')),
                ('right_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت راست انتهای سایت')),
                ('left_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت چپ انتهای سایت')),
                ('left_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت چپ انتهای سایت')),
                ('left_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت چپ انتهای سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات لندینگ اندروید',
                'verbose_name_plural': 'مدیریت تنظیمات لندینگ اندروید',
            },
        ),
        migrations.CreateModel(
            name='Setting_Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(blank=True, default=False, max_length=1000, verbose_name='تیتر دوره')),
                ('course_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات زیر تیتر دوره')),
                ('left_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت چپ')),
                ('right_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت راست')),
                ('title_of_document', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مدرک هاروارد')),
                ('david_video_title_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر روبه روی ویدئو david')),
                ('david_video_description_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات روبه روی ویدئو david')),
                ('course_feature_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی اول')),
                ('course_feature_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی اول')),
                ('course_feature_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی دوم')),
                ('course_feature_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی دوم')),
                ('course_feature_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی سوم')),
                ('course_feature_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی سوم')),
                ('course_feature_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی چهارم')),
                ('course_feature_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی چهارم')),
                ('course_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر سرفصل دوره')),
                ('course_under_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات زیر سر فصل دوره خط اول')),
                ('course_under_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات زیر سر فصل دوره خط دوم')),
                ('course_web_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره وب زیر سر فصل')),
                ('course_web_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط اول سرفصل وب')),
                ('course_web_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط دوم سر فصل وب')),
                ('course_web_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط سوم سرفصل وب')),
                ('course_web_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط چهارم سرفصل وب')),
                ('course_android_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره اندروید زیر سرفصل')),
                ('course_android_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط اول سرفصل اندروید')),
                ('course_android_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط دوم سر فصل اندروید')),
                ('course_android_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط سوم سرفصل اندروید')),
                ('course_android_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط چهارم سرفصل اندروید')),
                ('course_ai_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره هوش مصنوعی زیر سرفصل')),
                ('course_ai_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط اول سرفصل هوش مصنوعی')),
                ('course_ai_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط دوم سر فصل هوش مصنوعی')),
                ('course_ai_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط سوم سرفصل هوش مصنوعی')),
                ('course_ai_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح خط چهارم سرفصل هوش مصنوعی')),
                ('first_teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='نام اولین مدرس')),
                ('first_teacher_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات زیر نام اولین مدرس')),
                ('first_teacher_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='متن داخل دکمه اولین مدرس')),
                ('second_teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='نام دومین مدرس')),
                ('second_teacher_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات زیر نام دومین مدرس')),
                ('second_teacher_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='متن داخل دکمه دومین مدرس')),
                ('third_teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='نام سومین مدرس')),
                ('third_teacher_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات زیر نام سومین مدرس')),
                ('third_teacher_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='متن داخل دکمه سومین مدرس')),
            ],
            options={
                'verbose_name': 'تنظیمات لندینگ پکیج',
                'verbose_name_plural': 'مدیریت تنظیمات لندینگ پکیج',
            },
        ),
        migrations.CreateModel(
            name='Setting_Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(blank=True, default=False, max_length=1000, verbose_name='تیتر دوره')),
                ('course_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات زیر تیتر دوره')),
                ('left_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت چپ')),
                ('right_button', models.CharField(blank=True, default=False, max_length=256, verbose_name='دکمه سمت راست')),
                ('course_feature_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی اول')),
                ('course_feature_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی اول')),
                ('course_feature_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی دوم')),
                ('course_feature_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی دوم')),
                ('course_feature_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی سوم')),
                ('course_feature_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی سوم')),
                ('course_feature_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ویژگی چهارم')),
                ('course_feature_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات ویژگی چهارم')),
                ('david_video_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر زیر ویدئو david')),
                ('david_video_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول زیر ویدئو david')),
                ('david_video_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم زیر ویدئو david')),
                ('skills_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت ها')),
                ('skills_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت اول')),
                ('skill_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت اول')),
                ('skill_description1_1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت اول')),
                ('skills_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت دوم')),
                ('skill_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت دوم')),
                ('skill_description2_2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت دوم')),
                ('skills_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت سوم')),
                ('skill_description3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت سوم')),
                ('skill_description3_3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت سوم')),
                ('skills_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مهارت چهارم')),
                ('skill_description4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول مهارت چهارم')),
                ('skill_description4_4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم مهارت چهارم')),
                ('course_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر سرفصل دوره')),
                ('course_skill_topic', models.CharField(blank=True, default=False, max_length=256, verbose_name='عنوان دوره')),
                ('teacher_name', models.CharField(blank=True, default=False, max_length=256, verbose_name='اسم مدرس')),
                ('teacher_description', models.CharField(blank=True, default=False, max_length=1000, verbose_name='توضیحات مدرس')),
                ('suitable_for_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره مناسب چه افرادی است')),
                ('suitable_for_title1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح اول')),
                ('suitable_for_title2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح دوم')),
                ('suitable_for_title3', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح سوم')),
                ('suitable_for_title4', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیح چهارم')),
                ('title_of_document', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر مدرک هاروارد')),
                ('david_video_title_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر روبه روی ویدئو david')),
                ('david_video_description_under_register', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات روبه روی ویدئو david')),
                ('who_are_we_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر ما کی هستیم؟')),
                ('who_are_we_description1', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط اول ما کی هستیم')),
                ('who_are_we_description2', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات خط دوم ما کی هستیم')),
                ('right_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت راست انتهای سایت')),
                ('right_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت راست انتهای سایت')),
                ('right_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت راست انتهای سایت')),
                ('left_course_title', models.CharField(blank=True, default=False, max_length=256, verbose_name='تیتر دوره سمت چپ انتهای سایت')),
                ('left_course_description', models.CharField(blank=True, default=False, max_length=256, verbose_name='توضیحات دوره سمت چپ انتهای سایت')),
                ('left_course_price', models.CharField(blank=True, default=False, max_length=256, verbose_name='قیمت دوره سمت چپ انتهای سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات لندینگ وب',
                'verbose_name_plural': 'مدیریت تنظیمات لندینگ وب',
            },
        ),
        migrations.CreateModel(
            name='Web_sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titer', models.CharField(max_length=100, verbose_name='تیتر جلسه')),
                ('description', models.CharField(max_length=1000, verbose_name='متن کوتاه جلسه')),
                ('session_status', models.BooleanField(default=False, verbose_name='انتشار جلسه')),
                ('time', models.IntegerField(verbose_name='زمان هر جلسه بر حسب دقیقه')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک خلاصه متن')),
                ('question', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن سوال و جواب')),
                ('probelm_solve', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک کلاس رفع اشکال')),
                ('slide_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود اسلاید')),
                ('file_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود فایل')),
                ('note_download', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک دانلود جزوه')),
                ('session_image', models.CharField(max_length=500, null=True, verbose_name='تصویر جلسه')),
                ('first_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر اولین قسمت')),
                ('first_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک اولین ویدعو')),
                ('second_poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='پوستر دومین قسمت')),
                ('second_video_link', models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک دومین ویدعو')),
            ],
            options={
                'verbose_name': 'جلسات وب',
                'verbose_name_plural': 'جلسات وب',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('android', 'Android'), ('ai', 'Artificial Intelligence'), ('web', 'Web'), ('pack', 'Pack'), ('android-ins', 'Android Ins'), ('ai-ins', 'Artificial Intelligence Ins'), ('web-ins', 'Web Ins'), ('pack-ins', 'Pack Ins')], max_length=64)),
                ('customers', models.ManyToManyField(to='home.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('track_number', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PENDING', 'Transaction has just started'), ('FAILED', 'Transaction has failed'), ('SUCCESS', 'Transaction has successfully done')], default='PENDING', max_length=100)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.customer')),
                ('cuopon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.coupon')),
                ('customers', models.ManyToManyField(blank=True, related_name='customers', to='home.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.product')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_zarinpal.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='orders', to='home.Order'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.customer'),
        ),
    ]
