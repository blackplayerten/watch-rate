from django.contrib import admin
from . import models

# Register your models here.


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Film, FilmAdmin)
admin.site.register(models.Person)
admin.site.register(models.Role)
admin.site.register(models.Country)
admin.site.register(models.Genre)
admin.site.register(models.Vote)
