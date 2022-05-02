from django.shortcuts import render, redirect

# Add the following import
import uuid
import boto3 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime, Character
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
    character = Character.objects.filter(anime=anime_id)[:5]
    return render(request, 'animes/details.html', {'anime': anime, 'character': character})

@login_required
def characters_index(request, anime_id):
    character = Character.objects.filter(anime=anime_id)
    return render(request, 'characters/index.html', {'character': character})
  

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

def add_character(request, anime_id):
  form = CharacterForm(request.POST)
  if form.is_valid():
    new_character = form.save(commit=False)
    new_character.anime_id = anime_id
    new_character.save()
  return redirect('detail', anime_id = anime_id)

