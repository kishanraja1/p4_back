from django.urls import path
from . import views

urlpatterns = [
    path('api/albums', views.AlbumList.as_view(), name='album_list'), # api/Album will be routed to the AlbumList view for handling
    path('api/albums/<int:pk>', views.AlbumDetail.as_view(), name='album_detail'), # api/Album will be routed to the AlbumDetail view for handling
    path('api/albums/spotify_album', views.QueryAlbumList.as_view(), name="query_album_list")
]
