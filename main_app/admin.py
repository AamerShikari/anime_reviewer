from django.contrib import admin

# Register your models here.
from .models import Anime, Character

admin.site.register(Anime)
admin.site.register(Character)