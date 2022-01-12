from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, phone, name, last_name, email, password, **other_fields):
        if not phone:
            raise ValueError('شماره تماس یک فیلد اجباری است')
        if not name:
            raise ValueError('نام یک فیلد اجباری است')
        if not last_name:
            raise ValueError('نام خانوادگی یک فیلد اجباری است')
        if not email:
            raise ValueError('ادرس ایمیل یک فیلد اجباری است')
        user = self.model(phone=phone, name=name, last_name=last_name, email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, last_name, email, password=None, **other_fields):
        user = self.create_user(phone=phone, name=name, last_name=last_name, email=email,
                                password=password, **other_fields)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(max_length=11, verbose_name='شماره همراه')
    name = models.CharField(max_length=20, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    email = models.CharField(max_length=100, unique=True, verbose_name='ایمیل')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد کاربر')
    objects = MyUserManager()
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    is_admin = models.BooleanField(default=False, verbose_name='دسترسی ادمین')
    android = models.BooleanField(default=False, verbose_name='کلاس اندروید')
    web = models.BooleanField(default=False, verbose_name='کلاس وب')
    ai = models.BooleanField(default=False, verbose_name='کلاس هوش مصنوعی')
    field = models.CharField('رشته تحصیلی', null=True, max_length=100)
    age = models.CharField('سن',  max_length=300, null=True)
    address = models.TextField('ادرس', null=True)
    city = models.CharField('شهر', max_length=100, null=True)
    rezume = models.CharField('لینک رزومه', max_length=300, null=True, blank=True)
    postal_code = models.CharField('کد پستی', max_length=300, null=True, blank=True)
    linked_in = models.CharField('لینکدین', max_length=100, null=True, blank=True)
    static_phone = models.PositiveIntegerField('تلفن ثابت', null=True, blank=True)
    USERNAME_FIELD = 'email'
    complete_profile = models.BooleanField('تکمیل پروفایل', default=False)
    REQUIRED_FIELDS = ['name', 'last_name', 'phone']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin
