from django.contrib import admin
from .models import (
		Playlists, Playlist_songs, Song_Categories, Albums, Album_songs, HomePagePlaylists, HomePagePlaylists_songs, 
		Artists, UserArtists, UserPlaylists, UserPlaylists_songs, UserInheritedPlaylists, Song_model
		)
# Register your models here.

admin.site.register(Playlists)
admin.site.register(Playlist_songs)
admin.site.register(Song_Categories)
admin.site.register(Albums)
admin.site.register(Album_songs)
admin.site.register(HomePagePlaylists)
admin.site.register(HomePagePlaylists_songs)
admin.site.register(Artists)
admin.site.register(UserArtists)
admin.site.register(UserPlaylists)
admin.site.register(UserPlaylists_songs)
admin.site.register(UserInheritedPlaylists)
admin.site.register(Song_model)