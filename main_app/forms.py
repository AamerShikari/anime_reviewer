from django.forms import ModelForm

from .models import Review, Character

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

class CharacterForm(ModelForm):
    class Meta: 
        model = Character
        fields = ['name', 'description']
