function move(id) {
			
	var xhttp = new XMLHttpRequest();
	if(id == 1){
		history.pushState(1, null, "/")
		xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		    document.getElementById("block_content").innerHTML = this.responseText;
		  }
		};

		xhttp.open("GET", "/", true);
		xhttp.send();
					
	
	}else if(id == 2){
		history.pushState(2, null, "/show_favorite")
		xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		    document.getElementById("block_content").innerHTML = this.responseText;
		  }
		};

		xhttp.open("GET", "show_favorite", true);
		xhttp.send();
					
	}


}	