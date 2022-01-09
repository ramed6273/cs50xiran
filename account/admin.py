from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput())
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('phone', 'name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('پسوورد ها باید یکسان باشند')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = ('phone', 'name', 'last_name', 'email', 'password')

        def clean_password(self):
            return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'name', 'last_name', 'phone', 'android', 'ai', 'web', 'is_active', 'is_admin','complete_profile')
    list_filter = ('is_admin', 'is_active', 'ai', 'web', 'android')
    search_fields = ('email', 'phone')
    fieldsets = (
        (None, {'fields': (
            'phone', 'name', 'last_name', 'email', 'password', 'android', 'ai', 'web', 'is_active', 'field',
            'age', 'address', 'city', 'rezume', 'postal_code', 'linked_in', 'static_phone', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {'fields': (
        'phone', 'name', 'last_name', 'email', 'password1', 'password2', 'android', 'ai', 'web', 'is_active')}),
    )

    search_fields = ('phone', 'email')
    ordering = ('-created',)
    filter_horizontal = ()
    list_per_page = 20


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
