from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer
from .models import Artist
from django.http import HttpResponse, HttpResponseNotFound
from albums_api import spotify_client


# Create your views here.
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

def spotify_get_artist_info(request):
    json = {"field": "test", "example": "object"}
    print(request)
    return HttpResponse('<h1>Spotify get artist info requested</h1>')
