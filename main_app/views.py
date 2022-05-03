from django.shortcuts import render, redirect

# Add the following import
import uuid
import boto3 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime, Review
from .forms import ReviewForm
# from django.urls import reverse_lazy


from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    return render(request, 'animes/details.html', {'anime': anime,'form':form,'reviews':reviews})

    




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

def  add_review(request, anime_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.anime_id = anime_id
    new_review.save()
  
  return redirect('detail', anime_id=anime_id)

class ReviewDelete(DeleteView):
  model = Review
  success_url ='/animes/'
  # def get_success_url(self):
  #   anime_id = self.kwargs[anime_id]
  #   return reverse_lazy('details', kwargs={'anime_id':anime_id})
