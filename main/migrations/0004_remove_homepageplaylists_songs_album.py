# Generated by Django 3.1.3 on 2021-02-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210210_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageplaylists_songs',
            name='album',
        ),
    ]
