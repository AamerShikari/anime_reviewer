from django.contrib import admin

# Register your models here.
from .models import Anime, Review

admin.site.register(Anime)
admin.site.register(Review)
