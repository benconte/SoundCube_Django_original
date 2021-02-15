# Generated by Django 3.1.3 on 2021-02-10 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album_songs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='date_released',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='song_auther',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='song_img',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='song_name',
        ),
        migrations.RemoveField(
            model_name='album_songs',
            name='song_path',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='date_released',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='song_auther',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='song_img',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='song_name',
        ),
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='song_path',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='date_released',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='lyrics',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='reference_name',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='song_auther',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='song_category',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='song_img',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='song_name',
        ),
        migrations.RemoveField(
            model_name='playlist_songs',
            name='song_path',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='date_released',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='lyrics',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='song_auther',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='song_img',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='song_name',
        ),
        migrations.RemoveField(
            model_name='userplaylists_songs',
            name='song_path',
        ),
        migrations.AddField(
            model_name='album_songs',
            name='song_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_songs', to='main.song_model'),
        ),
        migrations.AddField(
            model_name='homepageplaylists_songs',
            name='song_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_page_playlist_songs', to='main.song_model'),
        ),
        migrations.AddField(
            model_name='playlist_songs',
            name='song_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlist_songs', to='main.song_model'),
        ),
        migrations.AddField(
            model_name='userplaylists_songs',
            name='song_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist_songs', to='main.song_model'),
        ),
    ]
