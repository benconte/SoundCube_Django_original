// getting total number of songs in playlists(length of playlist)
var total_songs = document.getElementsByTagName("tr");
var total_songs_holder = document.getElementById("playlist_songs_length");

total_songs_holder.innerHTML = (total_songs.length - 1) + " - tracks - 2hrs.35mins"