from django.contrib import admin
from musicapp.models import *

class ArtisteAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age"]

class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date_released", "likes"]

class LyricAdmin(admin.ModelAdmin):
    list_display = ["id", "song", "content"]


# Register your models here.

admin.site.register(Artiste, ArtisteAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Lyric, LyricAdmin)

