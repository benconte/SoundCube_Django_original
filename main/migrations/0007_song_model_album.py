# Generated by Django 3.1.3 on 2021-02-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_albums_album_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_model',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_model', to='main.albums'),
        ),
    ]
