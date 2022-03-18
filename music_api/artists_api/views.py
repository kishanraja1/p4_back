from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework import generics
from .serializers import ArtistSerializer
from .models import Artist
from albums_api import spotify_client


# Create your views here.
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

def spotify_get_artist_info(request):
    artist_query = spotify_client.spotify.search('John Prine','artist')
    artist_obj = spotify_client.spotify.convert_artist_data(artist_query)
    # print(request)
    return JsonResponse(artist_obj)
    # return JsonResponse({"default field":"default"})