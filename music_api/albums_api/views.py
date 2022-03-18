from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework import generics
from .serializers import AlbumSerializer
from .models import Album

# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = AlbumSerializer # tell django what serializer to use

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer

def spotify_get_album_info(request):
    my_obj = {"test_field":"hello", "test_2":"just testing"}
    return JsonResponse(my_obj)