#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req) #recup session
    redirectionSiNonConnecte(req,sess) #redirige si la session est nouvelle
    id_util=sess["id_util"] #recup l'id_util
    id_contact=req.form["id_contact"] #recup l'id_contact

#debut sql
    conn = connexionBD()
    cur = conn.cursor()
    sql = "select * from contact where id_contact={} and id_util={};".format(id_contact, id_util)
    cur.execute(sql)
    conn.commit()
    data = cur.fetchall()
    conn.close()
#fin sql

    if not data:
	req.write(codeHTML("Erreur !", """
<p>Ce contact ne vous appartient pas.</p>
""" + lien('menu.py',"Retour au menu")))
#si le resultat de la req sql est vide
#alors le contact n'appartient pas à l'utilisateur connecté

    else:
#début prise info dans les var
	data = data[0]
	nom=str(data[1])
	email=str(data[2])
	tel=str(data[3])
	addr=str(data[4])
	lat=str(data[5])
	lon=str(data[6])
#fin prise infos
	content = "" #ou tout le surplus va être ajouté (en plus du nom)

	if email != "":
		content += """
        <tr>
                <td>Email</td>
                <td>""" + lien("mailto:" + email , email) + """</td>
        </tr>

"""
#check si l'email est donné

	if tel != "":
		content += """
        <tr>
                <td>Telephone</td>
                <td>""" + tel + """</td>
        </tr>

"""
#check si le num est donné

	if addr != "":
		content += """
	<tr>
		<td>Adresse</td>
		<td>""" + addr + """</td>
	</tr>
"""
#check si l'addresse est donné


#debut affiche map
        if addr == "": #si pas d'adresse
                maps="<b>Adresse non précisé</b>"
	elif lat=="None" and lon=="None": #si le geocodage ne renvoit rien
		maps="<b>Emplacement indisponible</b>"
	else: #créé la map avec lat et lon de geocodage
		maps="""
<link rel="stylesheet" href="leaflet.css"/>
<script src="leaflet.js"></script> 
<div id="carte" style="width: 600px; height: 400px"></div>
<script>
	var map = L.map("carte");
	map.setView({lat: """ + lat + """, lon: """ + lon + """}, 10);
	url="https://{s}.tile.openstreetmap.org" + "/{z}/{x}/{y}.png";
	var layer = L.tileLayer(url);
	layer.addTo(map);
	var m = L.marker({lat: """ + lat + """, lon: """ + lon + """});
	m.addTo(map);
</script>
"""
#fin affichage maps

#la suite écrit la page avec les différentes variables données
	req.write(codeHTML("Fiche d'un contact","""
<b>Fiche d'un contact</b><br/>
<table>
        <tr>
                <td>Nom</td>
                <td>""" + nom + """</td>
        </tr>
""" + content + """
</table>
""" + maps + """
<br/>
""" + lien ("supression.py?id_contact=" + id_contact ,"Supression du contact") + """
<br/>
""" + lien("menu.py","Retour au menu")))
