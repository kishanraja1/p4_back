from django.shortcuts import render
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
