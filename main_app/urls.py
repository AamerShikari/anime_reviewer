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
	path('animes/<int:anime_id>/add_review/', views.add_review, name='add_review'),
	path('animes/<int:anime_id>/reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
	path('animes/<int:anime_id>/characters/add', views.character_adding, name='character_adding'),
	path('animes/<int:anime_id>/characters/create', views.CharactersCreate, name='characters_create'),
	path('animes/<int:anime_id>/characters/', views.characters_index, name='characters_index'),
	path('animes/<int:anime_id>/characters/<int:character_id>', views.character_detail, name='character_detail'),
	path('animes/<int:anime_id>/characters/<int:pk>/update/', views.character_update.as_view(), name='character_update'),
	path('animes/<int:anime_id>/characters/<int:pk>/delete/', views.character_delete.as_view(), name='character_delete'),
]