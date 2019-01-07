from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext_lazy as _


def is_valid_year(val):
    if not 1800 < val < datetime.today().year + 10:
        raise validators.ValidationError('Year should be real')


def is_valid_age(val):
    if not 0 <= val <= 21:
        raise validators.ValidationError('Year should be real')


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='img', verbose_name='Аватар')
    email = models.EmailField(blank=False, unique=True, verbose_name='Почта')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Film(models.Model):
    name = models.TextField(verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    producer = models.ManyToManyField(to='Person', related_name='m2m_producers', verbose_name='Продюсер')
    year = models.IntegerField(validators=[is_valid_year], verbose_name='Год')
    country = models.ManyToManyField(to='Country', verbose_name='Страна')
    genre = models.ManyToManyField(to='Genre', verbose_name='Жанр')
    actors = models.ManyToManyField(to='Person', related_name='m2m_actors', verbose_name='Актеры')
    age = models.IntegerField(blank=True, null=True, validators=[is_valid_age], verbose_name='Возраст')
    time = models.CharField(max_length=16, verbose_name='Время')
    user_rating = models.IntegerField(blank=True, default=1, verbose_name='Рейтинг')
    plot = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class FavoriteFilms(models.Model):
    uID = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Айди пользователя')
    fID = models.ForeignKey(to=Film, on_delete=models.CASCADE, verbose_name='Айди фильма')

    class Meta:
        unique_together = ('uID', 'fID')
        verbose_name = 'Избранный фильм'
        verbose_name_plural = 'Избранные фильмы'


class Person(models.Model):
    first_name = models.TextField(verbose_name='Имя')
    last_name = models.TextField(verbose_name='Фамилия')
    role = models.ManyToManyField(to='Role', verbose_name='Роль')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'


class Role(models.Model):
    name = models.TextField(verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Genre(models.Model):
    name = models.TextField(verbose_name='Название')
    about = models.TextField(verbose_name='О')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Country(models.Model):
    name = models.TextField(verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Vote(models.Model):
    mark = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)], verbose_name='Оценка')
    film = models.ForeignKey(to='Film', on_delete=models.CASCADE, verbose_name='Название')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
