document.addEventListener("DOMContentLoaded", function() { startplayer(); }, false);
var player = new Audio; //document.getElementById('music_player');
var isPlaying = false;
var re_playying = document.getElementById("re_play");
var own = document.getElementById('own');
let index = 0;//we use index to get the songs from musicData according to the skip


var song_path = 'static/uploads/Syn Cole - Feel Good - (Music Video).mp3';
let repeatMusic = false;
var rep_on = false;
var img = document.getElementById('img');
var son = document.getElementById('song');
var playing_song_name = document.getElementById("playing_song_name");



var plt_image = document.getElementById('plt_image');
var carousel_image_holder = document.getElementById('carousel_image_holder');

var lyrics_head = document.getElementById('lyrics_head');
var lyrics_artist = document.getElementById('lyrics_artist');
var lyrics = document.getElementById('lyrics');
var show_lyrics = document.getElementById('show_lyrics');
var show_queue_box = document.getElementById('queue_box');
var arrow_down = document.getElementById('arrow_down');

var is_show_lyrics = false;
var is_show_queue = false;

// --------------------------------------------------------------------------
var step_forwad = document.getElementById('step_forwad');
var step_backward = document.getElementById('step_backward');
var pausing = document.getElementById('pause');
var pause_btn = document.getElementById('pause_btn');
const progress = document.getElementById("progress");
var volumeBar = document.getElementById('volumeBar');
var volumedown_btn = document.getElementById("volumedown");
var volumeup_btn = document.getElementById("volumeup");
var mic = document.getElementById("mic");
var shufle = document.getElementById("shufle");
var queue = document.getElementById("queue");

let disabled = true;
// --------------------------------------------------------------------------
const musicData = [];
const queue_playlist = [];

// disabling buttons
pause_btn.setAttribute("disabled", disabled);
step_forwad.setAttribute("disabled", disabled);
step_backward.setAttribute("disabled", disabled);
progress.setAttribute("disabled", disabled);
volumeBar.setAttribute("disabled", disabled);
volumedown_btn.setAttribute("disabled", disabled);
volumeup_btn.setAttribute("disabled", disabled);
mic.style.visibility = "hidden";
shufle.setAttribute("disabled", disabled);
queue.setAttribute("disabled", disabled);
re_playying.style.visibility = "hidden";

// end of disabling buttons
player.type = 'audio/mpeg';
   

function startplayer() 
{
 
 player.controls = false;
}

function re_play(){
if (rep_on == false){
  rep_on = true;
  re_playying.style.color = 'red';
}
else{
  rep_on = false;
  re_playying.style.color = none;
}

}


function play(){
  if (musicData !== {}){
    if (isPlaying == false){
      isPlaying = true
      
      player.play();
      
      pausing.className = "fas fa-pause-circle fa-3x";

    }else{
      isPlaying = false
      player.pause();
      
      pausing.className = "fa fa-play-circle fa-3x";
    }
  }
}

let data = {};

const playMusic = async (i) => {
    if(data.id != i){
      index = i;
      data = musicData.find(m => m.id === i);// || musicData[1]
      player.src = data.src;
      await player.load();
      player.play();

      playing_song_name.innerHTML = data.name + ' - '+ data.song_auther;
  
      pausing.className = "fas fa-pause-circle fa-3x";
    }else{
      if (isPlaying == false){
        isPlaying = true;
        
        player.play();
        
        pausing.className = "fas fa-pause-circle fa-3x";
        

      }else{
        isPlaying = false
        player.pause();
        
        pausing.className = "fa fa-play-circle fa-3x";

      }

      // use for loop to check with id matches data.id from there change the icons. and also change the previous one
      document.getElementById(i).className = "fas fa-pause-circle fa-3x";
      document.getElementById(i).className = "fa fa-play-circle fa-3x";
    }
   

    
    pause_btn.removeAttribute("disabled");
    step_forwad.removeAttribute("disabled");
    step_backward.removeAttribute("disabled");
    progress.removeAttribute("disabled");
    volumeBar.removeAttribute("disabled");
    volumedown_btn.removeAttribute("disabled");
    volumeup_btn.removeAttribute("disabled");
    mic.style.visibility = "visible";
    shufle.removeAttribute("disabled");
    queue.removeAttribute("disabled");
    re_playying.style.visibility = "visible";
}


function showLyrics(i){
  var block_content = document.getElementById('block_content');

  if(data.id == i){
    if (isPlaying == true){
      isPlaying = false;
    }else{
      isPlaying = true;
      player.pause();
      
      pausing.className = "fa fa-play-circle fa-3x";
    }
  }else{
      isPlaying = true;
      
      player.play();
      
      pausing.className = "fas fa-pause-circle fa-3x";
  }

  if (is_show_queue == true) {
    show_queue_box.style.display = 'none';
    is_show_lyrics = true;
    show_lyrics.style.display = 'block';
    block_content.style.display = 'none';

  }
  else {
    is_show_lyrics = true;
    show_lyrics.style.display = 'block';
    block_content.style.display = 'none';
  }
  
  if(data.lyrics){
    lyrics_head.innerHTML = data.name;
    lyrics_artist.innerHTML = 'by. ' + data.song_auther;
    lyrics.innerHTML = data.lyrics;
  }else{
    noLyrics(data.name, data.song_auther);
  }
  

  // let counter = 0;
  // let s_lyrics = "";//1 line maximum 55
  // let lyrics_holder = data.lyrics;

  // // getting the lyrics length for the loop
  // for(var s = 0; s <= lyrics_holder.length; s++){
  //   s_lyrics += lyrics_holder[s];
  //   counter += 1;
    
  //   // check if counter is >= 55 if so the we add a new line if not we keep looping until we see a space
  //   if(counter >= 55){
  //     if(lyrics_holder[s] === ' '){
  //       counter = 0;
  //       s_lyrics += '<br />';
  //       continue;
  //     }
  //     else{
  //       counter +=1;
  //       continue;
  //     }
      
  //   }
  // }
  
  

}
function cancelLyrics(){
  var block_content = document.getElementById('block_content');
  is_show_lyrics = false;
  block_content.style.display = 'flex';
  show_lyrics.style.display = 'none';
}




function noLyrics(song_name, song_auther){
  var block_content = document.getElementById('block_content');

  if (isPlaying == false){
      isPlaying = true;
      
      player.play();
      
      pausing.className = "fas fa-pause-circle fa-3x";

    }else{
      isPlaying = false;
      player.pause();
      
      pausing.className = "fa fa-play-circle fa-3x";
    }

  if (is_show_queue == true) {
    show_queue_box.style.display = 'none';
    is_show_lyrics = true;
    show_lyrics.style.display = 'block';
    block_content.style.display = 'none';

  }
  else {
    is_show_lyrics = true;
    show_lyrics.style.display = 'block';
    block_content.style.display = 'none';
  }
  
  lyrics_head.innerHTML = data.name;
  lyrics_artist.innerHTML = 'by. ' + data.song_auther;

  let nolyrics_msg = `

        <center style="margin-top:200px;">

          This song has no lyrics.
          <i class="far fa-grin-beam-sweat"></i>
          <i class="far fa-frown ml-1"></i>
        <center/>
      `
  lyrics.innerHTML = nolyrics_msg;
}


// showing queue

function showQueueBox(){
  var block_content = document.getElementById('block_content');
  show_queue_box.style.display = 'block';
  block_content.style.display = 'none';
  is_show_queue = true;

  var queue_playlist_img = document.getElementById("queue_playlist_img");
  queue_playlist_img.setAttribute('src', queue_playlist[0].img);//since i added the playlist into an array, we have to pass in 0 because the playlist we want is the first one
  document.getElementById("playlist_name").innerHTML = queue_playlist[0].name;
  if(queue_playlist[0].artists){
    document.getElementById("playlist_artists").innerHTML = "by. " + queue_playlist[0].artists;
  }
  document.getElementById("tracks_length").innerHTML = musicData.length;
  var t_body = document.getElementById("queue_t_body");
  // adding songs to queue tables
  for(let q_song = 0; q_song <= musicData.length; q_song++){
    var tableData = document.createElement("tr");
    tableData.innerHTML = `<td><img src='` + musicData[q_song].img +`' class='queue_table_img'><i class="fa fa-play-circle" onclick='playMusic(`+q_song+`)'></i></td>
    <td>`+musicData[q_song].name+ `</td>
    <td><div><a href='/artist_data/`+ musicData[q_song].song_auther +`' class='queue-table-content'>`+musicData[q_song].song_auther+`</p></div></td>
    <td><img src="/static/main/img/mic_microphone.jpg" class="lyrics-icon rounded-circle" width="55" height="55" onclick='playMusic(`+q_song+`);showLyrics();'></td>
    <td><a href='/album/`+ musicData[q_song].album_id + `' class='queue-table-content'>`+ musicData[q_song].album +`</a></td>
    <td><i class="far fa-heart fa-2x"></i></td>
    <td>3.12</td>
    <td><button type='button'><i class="far fa-times-circle fa-2x queue_song_remove_icon"></i></button></td>`;
    t_body.appendChild(tableData)//adding the looped data to the html body tag
    
  }


}
function cancelQueueBox(){
  var block_content = document.getElementById('block_content');
  if (is_show_lyrics == true) {
    show_queue_box.style.display = 'none';
  } else {
    block_content.style.display = 'flex';
    show_queue_box.style.display = 'none';
  }
  
}

function queue_remove_song(q_song){
   musicData[q_song] = {}
  //  console.log(q_song)
}

const nextPlay = () => {
  index++;
  if (index >= musicData.length) {
   index = 0;
  }
  playMusic(index);
}

const prevPlay = () => {
  if (index <= 0) {
    index = musicData.length;
  }
  index--;
  playMusic(index);

}



// eventListners 
player.addEventListener("ended", () => {
  nextPlay();
});

const volumeDown = () => {
volumeBar.value = Number(volumeBar.value) - 20
player.volume = volumeBar.value / 100
}
const volumeUp = () => {
volumeBar.value = Number(volumeBar.value) + 20
player.volume = volumeBar.value / 100
}

const repeat = e => {
repeatMusic = !repeatMusic;
player.loop = repeatMusic;

if (rep_on == false){
  rep_on = true;
  re_playying.style.color = '#1DB954';
}
else{
  rep_on = false;
  re_playying.style.color = '#333';
}
}

player.onloadeddata = () =>  {
  progress.max = player.duration
  const ds = parseInt(player.duration % 60)//getting seconds
  const dm = parseInt((player.duration / 60) % 60)//getting minutes
  ttview.textContent = dm + ':' + ds;
}
player.ontimeupdate =  () =>  { 
  progress.value = player.currentTime ;
}
player.addEventListener('timeupdate', () => {
  progress.value = player.currentTime;
  var cs = parseInt(player.currentTime % 60)
  var cm = parseInt((player.currentTime / 60) % 60)
  ctview.textContent = cm + ':' + cs;
}, false);


// const changeProgressBar = () => { 
//  player.currentTime = progress.value;
// }
function changeProgressBar(rangeElement){ 
  // player.currentTime = parseInt(player.duration*rangeElement.value/100);
  // player.currentTime = player.duration*rangeElement.value/100;
  player.currentTime = progress.value;

}

var vol = document.getElementById("change_vol");
const changeVolume = () => { 
 player.volume = vol.value;
}

function stop_aud() 
{
 player.pause();
 player.currentTime = 0;
}
function change_vol()
{
 
  if (player.volume < 1) {
          player.volume += 0.1;
          console.log(player.volume);
      } else {
          player.volume = 1;
      }
}

// switching next song with song selected by the user
function switch_song(song_to_switch){
  var current_song_id = data.id;

  var song_to_switch_id = musicData[song_to_switch].id;
  var temp; // let's say song id is 9
  temp = musicData[current_song_id + 1]; //getting the next song

  // first switching the songs then there ids.
  musicData[current_song_id + 1] = musicData[song_to_switch];
  //when we do this the id doesn't change so we need to change manually
  musicData[current_song_id + 1].id = temp.id; 

  musicData[song_to_switch] = temp;
  musicData[song_to_switch].id = song_to_switch;

}
