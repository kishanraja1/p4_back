from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Album # tell django which model to use
        fields = ('id', 'name', 'year',)
