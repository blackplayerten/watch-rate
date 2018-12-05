from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django import forms
from . import models


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
    username = forms.CharField(
        label='Login',
        min_length=4,
        max_length=15,
        widget=forms.TextInput(attrs={
            'autofocus': 'true',
            'class': 'form-control',
            'placeholder': 'login',
            'id': 'login-pass',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'autofocus': 'true', 'class': 'form-control',
            'placeholder': 'e-mail',
            'id': 'login-pass',
        })
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'login-pass',
        }),
    )
    password2 = forms.CharField(
        label='Repeat password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'repeat password',
            'id': 'login-pass',
        }),
    )

    class Meta:
        model = models.User
        fields = ['username', 'email', 'avatar', ]
        widgets = {
            'avatar': forms.FileInput(attrs={
                'type': 'file',
                'class': 'choose-avatar',
                'id': 'Avatar',
            }),
        }


class SettingsForm(forms.ModelForm):
    username = forms.CharField(
        label='Login',
        min_length=4,
        max_length=15,
        widget=forms.TextInput(attrs={
            'autofocus': 'true',
            'class': 'form-control',
            'placeholder': 'login',
            'id': 'login-pass',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'autofocus': 'true', 'class': 'form-control',
            'placeholder': 'e-mail',
            'id': 'login-pass',
        })
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'login-pass',
        }),
        required=False
    )
    password2 = forms.CharField(
        label='Repeat password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'repeat password',
            'id': 'login-pass',
        }),
        required=False
    )

    def is_valid(self):
        return super().is_valid() and self.cleaned_data.get('password1') == self.cleaned_data.get('password2')

    class Meta:
        model = models.User
        fields = ['username', 'email', 'avatar', ]
        widgets = {
            'avatar': forms.FileInput(attrs={
                'type': 'file',
                'class': 'choose-avatar',
                'id': 'Avatar',
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        new_pass = self.cleaned_data.get('password1')
        if new_pass != '':
            user.set_password()
        if commit:
            user.save()
        return user
