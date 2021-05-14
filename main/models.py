from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Song_Categories(models.Model):
    category = models.CharField(max_length=200)
    category_color = models.CharField(max_length=200)
    category_img = models.ImageField(upload_to='category_images', default='category.jpg')

    def __str__(self):
        return f'Song_Categories({self.category}, {self.category_color})'

class Artists(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='art_img')
    followers_fans = models.ManyToManyField(User, related_name="followers_fans", blank=True)
    biography = models.TextField(null=True)

    def __str__(self):
        return f"Artists({self.name})"

    def total_followers(self):
        return self.followers_fans.count()

class Albums(models.Model):
    name = models.CharField(max_length=200)
    album_author = models.CharField(max_length=200)
    album_artist = models.ManyToManyField(Artists, blank=True, related_name="album_artist")
    album_img = models.ImageField(upload_to='album_imgs', default='playlist_icon.jpg')
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="album_name", blank=True)
    favorite = models.ManyToManyField(User, related_name="album_favorite", blank=True)


    def __str__(self):
        return f"Albums({self.name},{self.date_created})"

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

class Song_model(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='album_model',null=True, blank=True)
    song_name = models.CharField(max_length=200)
    song_auther_written = models.CharField(max_length=200)
    song_authers = models.ManyToManyField(Artists, blank=True,  related_name="song_authers")
    song_img = models.ImageField(upload_to='song_model_images')
    song_path = models.FileField(upload_to='song_model_songs')
    reference_name = models.CharField(max_length=200, null=True)
    date_released = models.DateTimeField(default=timezone.now)
    lyrics = models.TextField(null=True, blank=True)
    song_category = models.ForeignKey(Song_Categories, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="song_name", blank=True)
    favorite = models.ManyToManyField(User, related_name="favorite_song", blank=True)

    def __str__(self):
        return f"Song({self.song_name}, {self.song_auther_written}, {self.song_category})"

    def authers_as_list(self):
        artists_list = []
        for artists in self.song_authers.all():
            artists_list.append(artists.name)

        return artists_list
        
    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


class Album_songs(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='album',null=True)
    song_model = models.ForeignKey(Song_model, on_delete=models.CASCADE, null=True, related_name="album_songs")

    def __str__(self):
        return f"Album_songs({self.album.name}, {self.song_model.song_name}, {self.song_model.song_auther_written})"

    def get_absolute_url(self):
        return reverse('home')

class Playlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_playlists")
    name = models.CharField(max_length=200)
    inspired = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    playlist_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="playlist_author")
    playlist_img = models.ImageField(upload_to='playlist_images',default='playlist_icon.jpg')
    likes = models.ManyToManyField(User, related_name="playlist_name", blank=True)
    favorite = models.ManyToManyField(User, related_name="playlist_favorite", blank=True)

    def __str__(self):
        return f"Playlists({self.name},{self.inspired})"

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')


class Playlist_songs(models.Model):
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE, null=True, related_name="playlist")
    song_model = models.ForeignKey(Song_model, on_delete=models.CASCADE, null=True, related_name="playlist_songs")

    def __str__(self):
        return f"Playlist_songs({self.playlist.name}, {self.song_model.song_name}, {self.song_model.song_auther_written})"

    def get_absolute_url(self):
        return reverse('home')


class HomePagePlaylists(models.Model):
    name = models.CharField(max_length=200)
    inspired = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    playlist_img = models.ImageField(upload_to='playlist_images',default='default.jpg')

    def __str__(self):
        return f"HomePagePlaylists({self.name},{self.inspired})"

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

class HomePagePlaylists_songs(models.Model):
    playlist = models.ForeignKey(HomePagePlaylists, on_delete=models.CASCADE, null=True, related_name="homepageplaylist")
    song_model = models.ForeignKey(Song_model, on_delete=models.CASCADE, null=True, related_name="home_page_playlist_songs")

    def __str__(self):
        return f"HomePagePlaylists_songs({self.playlist.name}, {self.song_model.song_name}, {self.song_model.song_auther_written})"

    def get_absolute_url(self):
        return reverse('home')


class UserArtists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="user_choose_artists")
    userartist = models.ForeignKey(Artists, on_delete=models.CASCADE, null=True, blank=True, related_name='user_artist')

    def __str__(self):
        return f"UserArtists({self.userartist}, {self.user.username})"

class UserPlaylists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_created_playlists")
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    playlist_img = models.ImageField(upload_to='user_playlist_images',default='playlist_icon.jpg')
    likes = models.ManyToManyField(User, related_name="user_playlist_name", blank=True)
    favorite = models.ManyToManyField(User, related_name="user_playlist_favorite", blank=True)

    def __str__(self):
        return f"Playlists({self.user.username},{self.name})"

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

    # def save(self, *args, **kwargs):
    #     super(UserPlaylists,self).save(*args, **kwargs)

    #     img = Image.open(self.playlist_img.path)

    #     img.save(self.playlist_img.path)
    #     # if img.height > 300 or img.width > 300:
    #     #     output_size = (300, 300)
    #     #     img.thumbnail(output_size)
    #     #     # file path

class UserPlaylists_songs(models.Model):
    playlist = models.ForeignKey(UserPlaylists, on_delete=models.CASCADE, null=True, related_name="userplaylists")
    song_model = models.ForeignKey(Song_model, on_delete=models.CASCADE, null=True, related_name="user_playlist_songs")

    def __str__(self):
        return f"UserPlaylists_songs({self.playlist.name}, {self.song_model.song_name}, {self.song_model.song_auther_written})"

    def get_absolute_url(self):
        return reverse('home')


class UserInheritedPlaylists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="userInherited")
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE, null=True, related_name="userInheritedPlaylists")

    def __str__(self):
        return f"UserInheritedPlaylists('{self.playlist.name}', '{self.playlist.playlist_author}')"

    def get_absolute_url(self):
        return reverse('home')

class DiscoverPage_UserInheritedPlaylists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="discover_userInherited")
    playlist = models.ForeignKey(HomePagePlaylists, on_delete=models.CASCADE, null=True, related_name="discover_userInheritedPlaylists")

    def __str__(self):
        return f"DiscoverPage_UserInheritedPlaylists('{self.playlist.name}', '{self.playlist.playlist_author}')"

    def get_absolute_url(self):
        return reverse('home')


class Test(models.Model):
    art = models.ManyToManyField(Artists, blank=False, related_name="test_art")

    # def __str__(self):
    #     return ', '.join([a.name for a in self.art.all()])

    def all_artists(self):
        art_list = []
        for a in self.art.all():
            art_list.append(a.name)

        return art_list

class UserFriends(models.Model):
    user_friends = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='user_friends')
    friends = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='friends')

    def __str__(self):
        return f"UserFriends(user: {self.user_friends.username}, friends: {self.friends})"



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notification_receiver')
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='notification_sender_user')
    subject = models.CharField(max_length=500)
    msg = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    notification_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return f"Notification(receiver: {self.user.username}, sender: {self.sender_user.username}, {self.subject}, {self.date_sent}, {self.notification_read})"





"""
Jean Kayiranga
RWUNDP\jean.kayiranga

"""     