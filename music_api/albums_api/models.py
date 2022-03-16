from django.db import models
from artists_api.models import Artist

# Create your models here.
class Album(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    artist = models.ForeignKey('artists_api.Artist', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
