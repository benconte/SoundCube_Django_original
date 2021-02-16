from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import (
		Playlists, Playlist_songs, Song_Categories, Albums, HomePagePlaylists, HomePagePlaylists_songs, 
		Artists, UserArtists, UserPlaylists, UserPlaylists_songs, UserInheritedPlaylists, Song_model
		)
from .forms import CreateUserPlaylists, UserPlaylistsImgUpdate
import json
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

@login_required
def home(request):
	playlist = Playlists.objects.all()
	playlist2 = Playlists.objects.order_by('-date_created')#[:5]
	category = Song_Categories.objects.all()[:12]
	playlist_length = len(playlist)
	# pltlist = json.dumps(playlist)
	context = {
		'playlist': playlist,
		'playlist2': playlist2,
		'category': category,
		'playlist_length': playlist_length
	}
	return render(request, 'main/home.html', context)

def test(request):
	playlist = Playlist_songs.objects.all()
	playlista = Playlists.objects.all()
	context = {
		'playlista':playlista,
		'playlist':playlist
	}
	return render(request, 'main/test.html', context)

@login_required
def discover(request):
	playlist = HomePagePlaylists.objects.all()
	discover_playlist = HomePagePlaylists.objects.order_by('-date_created')
	category = Song_Categories.objects.all()
	context = {
		'category': category,
		'discover_playlist': discover_playlist,
		'playlist':playlist
	}
	return render(request, 'main/discover.html', context)

# @login_required
# def test(request):#,id
# 	# playlist = Playlist_songs.objects.all()#playlist = Playlists.objects.get(id=id)
# 	context = {
		
# 	}
# 	return render(request, 'main/test.html', context)

@login_required
def like_song(request, pk):
	song = get_object_or_404(Song_model, id=request.POST.get('song_id'))#getting the song which takes the like
	liked = False
	if song.likes.filter(id=request.user.id).exists():#check if the like has been liked by a specific user
		song.likes.remove(request.user)
		liked = False
	else:
		song.likes.add(request.user)
		liked = True

	return redirect('home')#, args=[str(pk)]
	# return HttpResponseRedirect(reverse('playlist', args=[str(pk)]))

@login_required
def favorite_song(request, id):
	song = get_object_or_404(Song_model, id=id)
	if song.favorite.filter(id=request.user.id).exists():
		song.favorite.remove(request.user)

	else:
		song.favorite.add(request.user)

	# return HttpResponseRedirect(reverse('playlist', args=[str(id)]))
	return redirect('show_favorite')


@login_required
def display_playlist_songs(request,id):
	playlist = Playlists.objects.get(id=id)
	
	if playlist:
		# first we get the playlist using filter.This will get a specific playlist
		stuff = Playlist_songs.objects.filter(playlist=playlist).all()
		# liked = False
		# song_liked_dict = {}
		# we create an array to hold the liked songs
		song_liked_list = []
		
		# then we loop through each song checking if the authenticated user has a like. If so we append it to the song_liked_list
		for song in stuff:
			if song.song_model.likes.filter(id=request.user.id).all():
				liked = True
				# song_liked_dict[f"{request.user.username}"] = f"{song.song_model.song_name}/liked"
				song_liked_list.append(f"{song.song_model.song_name}")
		print(song_liked_list)

		context = {
			'playlist': playlist,
			'song_liked_list':song_liked_list,
			'liked': liked,

		}
		return render(request, 'main/display_playlist.html', context)

@login_required
def display_discover_playlist_songs(request,id):
	# playlist = HomePagePlaylists.objects.get(id=id)
	playlist = get_object_or_404(HomePagePlaylists, id=id)
	

	if playlist:
		# first we get the playlist using filter.This will get a specific playlist
		stuff = HomePagePlaylists_songs.objects.filter(playlist=playlist).all()
		# liked = False
		# song_liked_dict = {}
		# we create an array to hold the liked songs
		song_liked_list = []
		
		# then we loop through each song checking if the authenticated user has a like. If so we append it to the song_liked_list
		for song in stuff:
			if song.song_model.likes.filter(id=request.user.id).all():

				# song_liked_dict[f"{request.user.username}"] = f"{song.song_model.song_name}/liked"
				song_liked_list.append(f"{song.song_model.song_name}")
		print(song_liked_list)

		context = {
			'playlist': playlist,
			'song_liked_list':song_liked_list,

		}
		return render(request, 'main/display_discover_playlist_songs.html', context)


@login_required
def search(request):
	if request.method == "GET":
		query = request.GET.get('query')

		if query:
			match = Song_model.objects.filter(song_name__icontains=query)

			if match:
				print("match found")
				context = {'match': match,
							'length': len(match),
						  }
				return render(request, "main/search.html", context)
			else:
				messages.error(request, 'no results found')
				print(dir(messages))
				return HttpResponseRedirect("/")

		else:
			messages.warning(request, 'Enter a search')
			return HttpResponseRedirect('/')

	return HttpResponseRedirect('/')


@login_required
def show_favorite(request):

	return render(request, 'main/favorites.html', {})

@login_required
def user_choose_fav_artist(request):
    artist = Artists.objects.all()
    if request.method == 'POST':
    	arts = request.POST.get('check_box')
    	plt = Artists.objects.get(name=arts)
    	userFavs = UserArtists(userartist=plt, user=request.user)
    	userFavs.save()
    	return redirect('/')

    	# plt = Artists.objects.get(name=arts)
    	# print(plt)

    context = {
    	'artists':artist
    }
    return render(request, 'main/choose_artists_page.html', context)

@login_required
def user_choose_fav_artist_search(request):
    if request.method == "GET":
    	query = request.GET.get('query')

    	if query:
    		match = Artists.objects.filter(name__icontains=query)

    		if match:
    			print("match found")
    			context = {
    				'artists': match,
    			}
    			return render(request, "main/choose_searched_artists_page.html", context)
    		else:
    			messages.warning(request, 'no artist found with that name')
    			return HttpResponseRedirect("choose_artist")

    	else:
    		messages.warning(request, 'Enter a search')
    		return HttpResponseRedirect('choose_artist')

    return HttpResponseRedirect('choose_artist')


@login_required
def user_playlist(request, username):
	return render(request, 'main/user_playlists.html', {})



# class CreatePlaylistView(LoginRequiredMixin,CreateView):
# 	model = UserPlaylists
# 	form_class = CreateUserPlaylists
# 	# fields = '__all__'
# 	template_name = 'main/userplaylists_form.html'

# 	def form_valid(self, form):
# 		# form.instance.user_id = self.kwargs['id']
# 		form.instance.user = self.request.user
# 		return super().form_valid(form)

# 	success_url = reverse_lazy('home')

class CreateUserPlaylistView(LoginRequiredMixin,CreateView):
	model = UserPlaylists
	fields = ['name','playlist_img']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class DeleteUserPlaylistView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = UserPlaylists
	success_url = '/'
	success_message = "Playlist deleted successfully!!"


	def test_func(self):
		playlist = self.get_object()
		if self.request.user == playlist.user:
			return True
		return False

# class ChangeUserPlaylist_Img(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
# 	model = UserPlaylists
# 	fields = ["playlist_img"]

# 	def form_valid(self, form):
# 		form.instance.user = self.request.user
# 		return super().form_valid(form)

# 	def test_func(self):
# 		post = self.get_object()
# 		if self.request.user == post.user:
# 			return True
# 		return False


@login_required
def display_user_playlist_songs(request,id):
	playlist = UserPlaylists.objects.get(id=id)
	if request.method == 'POST':
		p_form = request.POST.get("playlist_img")
		playlist.playlist_img = "user_playlist_images/"+p_form

		playlist.save()
		messages.success(request, f"Playlist {playlist.name} updated successfully")
		return redirect('home')

	if playlist:
		# first we get the playlist using filter.This will get a specific playlist
		stuff = UserPlaylists_songs.objects.filter(playlist=playlist).all()
		
		liked = False
		# song_liked_dict = {}
		# we create an array to hold the liked songs
		song_liked_list = []
		
		# then we loop through each song checking if the authenticated user has a like. If so we append it to the song_liked_list
		for song in stuff:
			if song.song_model.likes.filter(id=request.user.id).all():

				# song_liked_dict[f"{request.user.username}"] = f"{song.song_model.song_name}/liked"
				song_liked_list.append(f"{song.song_model.song_name}")
		print(song_liked_list)

		context = {
				'playlist': playlist,
				"song_liked_list": song_liked_list,
				
		}

		return render(request, 'main/display_user_playlist.html', context)

def savePlaylistToLibrary(request, id):
	#adding songs from home page playlists to playlist the user choosed
	get_playlist = get_object_or_404(Playlists,  id=id)
	if(get_playlist):
		if (UserInheritedPlaylists.objects.filter(user=request.user, playlist=get_playlist)).exists():
			db = UserInheritedPlaylists.objects.get(user= request.user, playlist=get_playlist)
			db.delete()
			messages.success(request, f'Playlist ({get_playlist.name}) removed from library successfully!')
		else:
			db = UserInheritedPlaylists(user= request.user, playlist=get_playlist)
			db.save()
			messages.success(request, f'Playlist ({get_playlist.name}) added to library successfully!')

		return redirect("home")

	else:
		messages.error(request, f'Error adding ({get_playlist.name}) to library, Please Try again after a while!')
		return redirect("home")


def add_song_to_user_playlist(request, playlist, id):
	if request.method == 'POST':
		#getting playlist we want to add the song to
		user_returned_playlist = get_object_or_404(UserPlaylists, id=playlist)# getting playlist
		get_song = get_object_or_404(Song_model, id=id)#song we want to add to playlist

		# Checking if a playlist aleardy has the song before adding it
		if( UserPlaylists_songs.objects.filter(playlist=user_returned_playlist, song_model=get_song)).first():
			messages.error(request, f'Can\'t add song to playlist ({user_returned_playlist.name}) because song already exist!')

			return redirect("home")
		else:
			db = UserPlaylists_songs(playlist= user_returned_playlist, song_model=get_song)
			db.save()

			messages.success(request, f'Song added to playlist ({user_returned_playlist.name}) successfully!')

			# return HttpResponseRedirect(reverse('playlist', args=[str(id)]))
			return redirect('home')
	else:
		messages.error(request, f'Error adding {get_song.song_name} to playlist {playlist.name}, Please Try again after a while!')
		# return HttpResponseRedirect(reverse('playlist', args=[str(id)]))
		return redirect('home')

@login_required
def remove_song_from_playlist(request, playlist, id):
	if request.method == 'POST':
		#getting playlist we want to add the song to
		user_returned_playlist = get_object_or_404(UserPlaylists, id=playlist)# getting playlist
		get_song = get_object_or_404(Song_model, id=id)#song we want to remove from playlist

		song = UserPlaylists_songs.objects.filter(playlist=user_returned_playlist, song_model=get_song).first()
		# Checking if a playlist aleardy has the song before adding it
		if(song):
			song.delete()
			messages.success(request, f'Song removed from playlist ({user_returned_playlist.name}) successfully!')

			return redirect("home")
		else:
			messages.error(request, f'Error removing ({user_returned_playlist.name}) from playlist!')
			return redirect("home")
	else:
		messages.error(request, f'Error adding {get_song.song_name} to playlist, Please Try again after a while!')
		return redirect("home")

# messages.error(request, f'Can\'t add song to playlist ({user_returned_playlist.name}) because song already exist!')

@login_required
def settings(request):
	return render(request, "main/settings.html", {})