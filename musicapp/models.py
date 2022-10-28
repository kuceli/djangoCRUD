from tabnanny import verbose
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural='Artists'
    
    def __str__(self): 
        return f"{self.first_name}   {self.last_name}   {self.age} "

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField(auto_now=False)
    likes = models.IntegerField()
    # artiste_id = models.IntegerField()

    def __str__(self): 
        return f"{self.title}"

class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    # song_id = models.IntegerField() 

    def __str__(self): 
        return f"{self.song.title}   {self.content}"