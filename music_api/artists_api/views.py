from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, request, status

from .serializers import ArtistSerializer, QueryArtistSerializer
from .models import Artist, QueryArtist
from albums_api import spotify_client


# Create your views here.

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

@ensure_csrf_cookie
def spotify_get_artist_info(request):
    search_query = request.POST.get('searchQuery')
    artist_query = spotify_client.spotify.search(f'{search_query}','artist')
    artist_obj = spotify_client.spotify.convert_artist_data(artist_query)
    # print(artist_obj)
    # return JsonResponse({"default field":"default"})
    return JsonResponse(artist_obj)

class QueryArtistList(APIView):
    def post(self, request):
        search_query = request.data['search_query']
        print(search_query)
        artist_query = spotify_client.spotify.search(f'{search_query}','artist')
        artist_obj = spotify_client.spotify.convert_artist_data(artist_query)
        print(artist_obj)
        return JsonResponse(artist_obj)