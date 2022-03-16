from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer
from .models import Artist

# Create your views here.
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer
