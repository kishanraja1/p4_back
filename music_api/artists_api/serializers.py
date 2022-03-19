from rest_framework import serializers
from .models import Artist, QueryArtist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'image',)

class QueryArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryArtist
        fields = ('id', 'search_query')
