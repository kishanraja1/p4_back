from rest_framework import serializers
from .models import Album, QueryAlbum

class AlbumSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Album # tell django which model to use
        fields = ('id', 'name', 'year', 'image',)

class QueryAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryAlbum
        fields = ('id', 'search_query')