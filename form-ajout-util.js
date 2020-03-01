function isItGood(){

        var login = document.getElementById("login");

        if (login.value == ""){
                alert("Erreur: Le login est requis.")
                return false
        }
	
	var mdp = document.getElementById("motdepasse");
	
	if (mdp.value == ""){
		alert("Erreur : Le mot de passe doit être renseigné")
		return false
	}else if (mdp.value.length <= 8 ){
	        alert("Erreur: Le mot de passe n'est pas assez long.")
                return false;
	}

	var conf = document.getElementById("conf");

        if (conf.value != mdp.value){
                alert("Erreur: Les mots de passe sont différents.")
                return false
        }
}

function alreadyUsed(){
	var login = document.getElementById("login");
	var url = "check-login.py?login=" + login.value;

    	var req = new XMLHttpRequest();
    	req.open("GET", url, true);

    	req.onreadystatechange = function(){
        	if(req.readyState == 4 && req.status == 200) {
			var used=document.getElementById("used") ;
                        used.innerHTML = req.responseText;
        	}

    	}
req.send();
}
