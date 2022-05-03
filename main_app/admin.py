from django.contrib import admin

# Register your models here.

from .models import Anime, Character, Review

admin.site.register(Anime)
admin.site.register(Character)
admin.site.register(Review)

