from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django import forms
from django.utils.text import slugify
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
            'class': 'form-control',
            'placeholder': 'e-mail',
            'id': 'login-pass',
        }),
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
            user.set_password(new_pass)
        if commit:
            user.save()
        return user


class AddFilmForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'required-field'}),
    ),

    producer = forms.ModelMultipleChoiceField(
        label='Producer',
        queryset=models.Person.objects.filter(role__name='Producer').all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }),
        required=False,
    )
    country = forms.ModelMultipleChoiceField(
        label='Country',
        queryset=models.Country.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }),
        required=False,
    )
    genre = forms.ModelMultipleChoiceField(
        label='Genre',
        queryset=models.Genre.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }),
        required=False,
    )
    actors = forms.ModelMultipleChoiceField(
        label='Actors',
        queryset=models.Person.objects.filter(role__name='Актер').all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }),
        required=False,
    )

    def save(self, commit=True):
        film = super().save(commit)
        if commit:
            film.slug = slugify(str(film.pk) + "-" + film.name)
            film.save()
        return film

    class Meta:
        model = models.Film
        fields = ['name', 'producer', 'year', 'country', 'genre', 'actors', 'age', 'time', 'plot', 'image', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
             }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'actors': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'plot': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'type': 'file',
                'class': 'choose-avatar',
                'id': 'image_film',
            }),
        }


# class AddFavorites(forms.ModelForm):
    # add =
