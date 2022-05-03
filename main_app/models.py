
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 


# from django.urls import reverse
# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id':self.id})


class Review(models.Model):
    content = models.CharField(max_length=1000)
    # rating = models.IntegerField(max_length=1)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
        )
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=2048)
    quote = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} from {self.anime}"

    def get_absolute_url(self):
        return reverse('character_detail', kwargs={'anime_id':self.anime.id, 'character_id':self.id})

