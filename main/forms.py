from django import forms
from django.contrib.auth.models import User
from .models import Playlists, UserPlaylists


class CreateUserPlaylists(forms.ModelForm):
	class Meta:
		model = UserPlaylists
		fields = ('name', 'playlist_img')

		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control'}),
			
		}


class UserPlaylistsUpdate(forms.ModelForm):
    class Meta:
        model = UserPlaylists
        fields = ['name'] 


class UserPlaylistsImgUpdate(forms.ModelForm):
    class Meta:
        model = UserPlaylists
        fields = ['playlist_img']