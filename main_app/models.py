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
        return f"{self.title} is a {self.category}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id':self.id})

RATINGS = (
    ('1','1:Very Bad'),
    ('2','2:Bad'),
    ('1','3:OK'),
    ('1','4.Good'),
    ('1','5.Excellent'),
)

class Review(models.Model):
    content = models.CharField(max_length=1000)
    # rating = models.IntegerField(max_length=1)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=RATINGS,
        default=RATINGS[0][0]
        )
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


   
