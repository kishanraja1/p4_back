from django.urls import path
from . import views

urlpatterns = [
    path('api/artists', views.ArtistList.as_view(), name='artist_list'),
    path('api/artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('api/artists/spotify_artist', views.QueryArtistList.as_view(), name="query_artist_list")
]
