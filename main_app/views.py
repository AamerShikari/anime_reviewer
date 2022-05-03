from django.shortcuts import render, redirect

# Add the following import
import uuid
import boto3 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime, Review, Character
from .forms import ReviewForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CharacterForm


# Define the home view
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST': 
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else: 
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def animes_index(request):
    animes = Anime.objects.filter(user=request.user)
    return render(request, 'animes/index.html', {'animes': animes})
  
@login_required
def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)

    form = ReviewForm()
    reviews = Review.objects.filter(anime=anime_id)
    character = Character.objects.filter(anime=anime_id)[:5]
    return render(request, 'animes/details.html', {'anime': anime,'form':form,'reviews':reviews, 'character': character})

@login_required
def characters_index(request, anime_id):
    character = Character.objects.filter(anime=anime_id)
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'characters/index.html', {'character': character, 'anime':anime})

@login_required
def character_detail(request, anime_id, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', {'character': character})

class character_update(LoginRequiredMixin, UpdateView):
  model = Character
  fields =['name','description']

class character_delete(LoginRequiredMixin, DeleteView):
  model = Character
  success_url = '/animes/'

class AnimeCreate(LoginRequiredMixin, CreateView):
  model = Anime
  fields =['title','category','language','description']
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the anime
    return super().form_valid(form)

class AnimeUpdate(LoginRequiredMixin, UpdateView):
  model = Anime
  fields =['category','language','description']
  
class AnimeDelete(LoginRequiredMixin, DeleteView):
  model = Anime
  success_url = '/animes/'

@login_required
def  add_review(request, anime_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.anime_id = anime_id
    new_review.save()
  
  return redirect('detail', anime_id=anime_id)

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url ='/animes/'

@login_required
def CharactersCreate(request, anime_id):
  form = CharacterForm(request.POST)
  if form.is_valid():
     new_char = form.save(commit=False)
     new_char.anime_id = anime_id
     new_char.save()
  return redirect('detail', anime_id)

@login_required
def character_adding(request, anime_id):
  char_form = CharacterForm()
  return render(request, 'main_app/charcterAddingForm.html', {'anime_id':anime_id, 'char_form': char_form})

