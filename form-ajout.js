function isItGood(){

        var nom = document.getElementById("nom");
        
	if (nom.value == ""){ 
                alert("Erreur: Le nom est requis.");
                return false;
	}

	var tel=document.getElementById("telephone");

	if (tel.value != ""){
        
		if (tel.value.length != 10){
                        alert("Erreur : Le numéro de téléphone doit contenir 10 caractères.");
                        return false;
		
		} else if (isNaN(tel.value)){
			alert("Erreur : Veuillez composez des nombres.");
			return false;
		}
	}
	
	var email=document.getElementById("email");

        if (email.value != ""){

                if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)){
                        return true;
                } else {
                        alert("Erreur : Email invalide.");
                        return false;
                }
        }

}
