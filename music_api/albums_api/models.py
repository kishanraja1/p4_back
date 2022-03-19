from django.db import models
from artists_api.models import Artist

# Create your models here.
class Album(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    image = models.TextField(default='')

class QueryAlbum(models.Model):
    search_query = models.TextField(default="untitled album")