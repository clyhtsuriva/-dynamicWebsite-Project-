function filtre(){

    var query = document.getElementById("nom");
    var url = "affiche-maps.py?nom=" + nom.value;

    var req = new XMLHttpRequest();
    req.open("GET", url, true);

    req.onreadystatechange = function(){
        if(req.readyState == 4 && req.status == 200) {
            var map=document.getElementById("carteRempl") ;
            map.innerHTML = req.responseText;
	    alert("")
        }

    }
req.send();
}

