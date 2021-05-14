from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
	path('', views.home, name="home"),
	path('savePlaylistToLibrary/<int:id>', views.savePlaylistToLibrary, name="savePlaylistToLibrary"),
	path('saveDiscoverPlaylistToLibrary/<int:id>', views.saveDiscoverPlaylistToLibrary, name="saveDiscoverPlaylistToLibrary"),
	path('add_song_playlist/<int:playlist>/<int:id>', views.add_song_to_user_playlist, name="add_song_to_playlist"),
	path('remove_song_playlist/<int:playlist>/<int:id>', views.remove_song_from_playlist, name="remove_song_from_playlist"),
	path(f'library/<str:username>', views.user_playlist, name='user_playlist'),
	path('choose_artist', views.user_choose_fav_artist, name="choose_artist"),
	path("user_choose_fav_artist_search", views.user_choose_fav_artist_search, name="user_choose_fav_artist_search"),
	path('discover', views.discover, name="discover"),
	path('clear_notifications', views.clear_notifications, name='clear_notifications'),
	path('clear_specific_notifications/<int:id>', views.clear_specific_notifications, name='clear_specific_notifications'),
	path('get_new_notifications', views.get_new_notifications, name='get_new_notifications'),
	path('search', views.search, name="search"),
	path('test', views.test, name="test"),#path('test/<int:id>', views.test, name="test"),
	path('playlist/<int:id>', views.display_playlist_songs, name="playlist"),
	path('album/<int:id>', views.display_album_songs, name="album"),
	path('discover/playlist/<int:id>', views.display_discover_playlist_songs, name="discover_playlists"),
	path('user_playlist/<int:id>', views.display_user_playlist_songs, name="display_user_playlist_songs"),
	path('like/<int:pk>', views.like_song, name="like_song"),
    path('favorite/<int:id>', views.favorite_song, name="favorite_song"),
    path('show_favorite', views.show_favorite, name="show_favorite"),
    path('create_user_playlist/<int:id>', views.CreateUserPlaylistView.as_view(), name='create_playlist'),			
    path('delete_user_playlist/<int:pk>', views.DeleteUserPlaylistView.as_view(), name='delete_user_playlist'),
    path('settings', views.settings, name="settings"),
	path("artist/<str:name>", views.get_artists_data, name="artist_data"),
	path("add_artist_followers/<str:name>", views.add_artist_followers, name="add_artist_followers"),
	# path("user_update_playlist/<int:pk>", views.UserPlaylistUpdateView.as_view(), name="user_update_playlist")
]
