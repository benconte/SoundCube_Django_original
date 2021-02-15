from django.test import TestCase

# Create your tests here.
{% for plt in playlist.playlist.all %}
				musicData[{{forloop.counter0}}] = {id:{{forloop.counter0}}, name: "{{plt.song_model.song_name}}", img:"{{plt.song_model.song_img.url}}", src:"{{plt.song_model.song_path.url}}", song_auther: "{{plt.song_model.song_auther}}", lyrics:`{{plt.song_model.lyrics}}`}

			{% endfor %}