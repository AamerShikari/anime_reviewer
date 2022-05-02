from email.mime import image
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

class Characters(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

	def __str__(self):
		# this method will gives us the friendly meal choices value, so like Breakfast instead of B
		return f"{self.get_meal_display()} on {self.date}"

	class Meta:
		ordering = ['-date']