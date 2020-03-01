function cherche(){

    var nom = document.getElementById("nom");
    var url = "affiche-liste.py?nom=" + nom.value;

    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    
    req.onreadystatechange = function(){
	if(req.readyState == 4 && req.status == 200) {
	    var liste=document.getElementById("liste") ;
	    liste.innerHTML = req.responseText;
	}

    }
req.send();
}
