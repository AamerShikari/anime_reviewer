from django.forms import ModelForm
from .models import Character

class CharacterForm(ModelForm):
    class Meta: 
        model = Character
        fields = ['name', 'description']