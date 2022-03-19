from django.db import models
# from albums_api.models import Album

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    genre = models.TextField()
    image = models.TextField(default='')

    def __str__(self):
        return self.name

class QueryArtist(models.Model):
    search_query = models.TextField(default="No artist entered")

