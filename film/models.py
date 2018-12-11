from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.datetime_safe import datetime


def is_valid_year(val):
    if not 1800 < val < datetime.today().year + 10:
        raise validators.ValidationError('Year should be real')


def is_valid_age(val):
    if not 0 <= val <= 21:
        raise validators.ValidationError('Year should be real')


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='img')
    favorite_films = models.ManyToManyField(to='Film')


User._meta.get_field('email')._unique = True


class Film(models.Model):
    name = models.TextField()
    slug = models.SlugField()
    producer = models.ManyToManyField(to='Person', related_name='m2m_producers')
    year = models.IntegerField(validators=[is_valid_year])
    country = models.ManyToManyField(to='Country')
    genre = models.ManyToManyField(to='Genre')
    actors = models.ManyToManyField(to='Person', related_name='m2m_actors')
    age = models.IntegerField(blank=True, null=True, validators=[is_valid_age])
    time = models.CharField(max_length=16)
    user_rating = models.IntegerField(blank=True, default=1)
    plot = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='img')

    def __str__(self):
        return self.name




class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    role = models.ManyToManyField(to='Role')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Role(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    mark = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)])
    film = models.ForeignKey(to='Film', on_delete=models.CASCADE)
    # user = models.ForeignKey(to='UserProfile')

    # class Meta:
    #     unique_together = ('film', 'user')
