from django import forms
# from django.contrib.auth import get_user_model
# from account.models import User as account
# User = get_user_model()
from account.models import User
from home.models import Ai_sessions


class UpdateAccount(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "last_name", "email", "phone", 'field', 'age', 'city', 'rezume', 'postal_code', 'linked_in',
                  'static_phone', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].disabled = True
        self.fields["last_name"].disabled = True
        self.fields["email"].disabled = True
        self.fields["phone"].disabled = True
# reset password
class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Old Password'
    }))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'New Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'
    }))
