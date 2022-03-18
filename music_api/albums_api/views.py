from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, request
from .serializers import AlbumSerializer
from .models import Album
from albums_api import spotify_client


# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = AlbumSerializer # tell django what serializer to use

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer

@ensure_csrf_cookie
def spotify_get_album_info(request):
    print(request.POST)
    search_query = request.POST.get('searchQuery')
    print(search_query)
    album_query = spotify_client.spotify.search(f'{search_query}','album')
    album_obj = spotify_client.spotify.convert_album_data(album_query)
    # print(album_obj)
    # my_obj = {"test_field":"hello", "test_2":"just testing"}
    return JsonResponse(album_obj)