from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# from django.urls import reverse
# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} is a {self.category}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id':self.id})