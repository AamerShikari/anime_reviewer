from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'), #example path
	path('about/', views.about, name='about'),
	path('animes/', views.animes_index, name='index'),
	path('animes/<int:anime_id>/', views.animes_detail, name='detail'),
	path('animes/<int:pk>/delete/', views.AnimeDelete.as_view(), name='animes_delete'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', views.signup, name='signup'),
	path('animes/create/', views.AnimeCreate.as_view(), name='animes_create'),
	path('animes/<int:pk>/update/', views.AnimeUpdate.as_view(), name='animes_update'),

	

]