from django import forms
from django.contrib.auth.models import User
from django.core import validators

from zoomit_accounts.models import ProfileImage


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام کاربری'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور'}
        )
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput()
    )

    last_name = forms.CharField(
        widget=forms.TextInput()
    )

    email = forms.CharField(
        widget=forms.TextInput(),
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    username = forms.CharField(
        widget=forms.TextInput()
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        username_exist = User.objects.filter(username=user_name).exists()
        if username_exist:
            raise forms.ValidationError('نام کاربری وارد شده قبلا ثبت شده است')

        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=email).exists()
        if email_exist:
            raise forms.ValidationError('ایمیل وارد شده قبلا ثبت شده است')

        return email


class ProfilePictureForm(forms.Form):
    image = forms.ImageField(
        label='انتخاب تصویر'
    )


class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'}),
        label='تخلص'
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'}),
        label='نام کاربری',
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )
