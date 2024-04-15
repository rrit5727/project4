from django.db import models
from django.urls import reverse

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=100,
        default='Pop'
    )

    def __str__(self):
        return self.name


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
    occurence = models.IntegerField(default=0)

    def __str__(self):
        return self.name