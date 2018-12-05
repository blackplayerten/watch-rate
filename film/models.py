from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='img', default='img/ketnipz.png')
    favorite_films = models.ManyToManyField(to='Film')


class Film(models.Model):
    name = models.TextField()
    slug = models.SlugField()
    producer = models.ManyToManyField(to='Person', related_name='m2m_producers')
    year = models.DateField()
    country = models.ManyToManyField(to='Country')
    genre = models.ManyToManyField(to='Genre')
    actors = models.ManyToManyField(to='Person', related_name='m2m_actors')
    age = models.IntegerField()
    time = models.CharField(max_length=16)
    user_rating = models.FloatField(blank=True)
    plot = models.TextField()
    image = models.ImageField(blank=True)

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
