from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='Login',
        min_length=4,
        max_length=15,
        widget=forms.TextInput(attrs={
            'autofocus': 'true', 'class': 'form-control',
            'placeholder': 'login',
            'id': 'login-pass',
        }),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'login-pass',
        }),
    )


class CreateAccount(UserCreationForm):
    login = UsernameField(
        label='Login*',
        min_length=4,
        max_length=15,
        widget=forms.TextInput(attrs={
            'autofocus': 'true', 'class': 'form-control',
            'placeholder': 'login',
            'id': 'login-pass',
        }),
    )
    e_mail = forms.CharField(
        label='E-mail*',
        widget=forms.TextInput(attrs={
            'autofocus': 'true', 'class': 'form-control',
            'placeholder': 'e-mail',
            'id': 'login-pass',
        }),
    )
    password = forms.CharField(
        label='Password*',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'login-pass',
        }),
    )
    avatar = forms.FileInput(attrs={
            'class': 'choose-avatar',
            'id': 'Avatar',
        }
    )
