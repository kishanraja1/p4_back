from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    genre = models.TextField()
    soloArtists = models.BooleanField()
    language = models.TextField()
