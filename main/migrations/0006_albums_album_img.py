# Generated by Django 3.1.3 on 2021-02-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_discoverpage_userinheritedplaylists'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='album_img',
            field=models.ImageField(default='playlist_icon.jpg', upload_to='album_imgs'),
        ),
    ]
