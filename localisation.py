#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req) #recup session
    redirectionSiNonConnecte(req,sess) #redirige si la session est nouvelle
    id_util=sess["id_util"] #recup l'id_util

#sqlstart
    conn = connexionBD()
    cur = conn.cursor()
    sql = "select * from contact where id_util={} and latitude is not null and longitude is not null;".format(id_util)
#ajout des deux (lon et lat) pour être sur si jamais il y a un bug avec un seul des deux renseigné
    cur.execute(sql)
    conn.commit()
    data = cur.fetchall()
    conn.close()
#sqlend

#mapstart    
    maps="""
<link rel="stylesheet" href="leaflet.css"/>
<script src="leaflet.js"></script> 
<div id="carte" style="width: 600px; height: 400px"></div>
<script>
        var map = L.map("carte");
        map.setView({lat: 0 , lon: 0}, 1);
        url="https://{s}.tile.openstreetmap.org" + "/{z}/{x}/{y}.png";
        var layer = L.tileLayer(url);
        layer.addTo(map);
"""#initialise tous ce qui ne changera pas

#debut prise donné par contact
    for i in range(len(data)):
	lat=str(data[i][5])
	lon=str(data[i][6])
	id_contact=str(data[i][0])
	nom=str(data[i][1])
	maps+="""
var m = L.marker({lat: """ + lat + """, lon: """ + lon + """});
        m.addTo(map);
	m.bindPopup('<a href="fiche.py?id_contact=""" + id_contact + """">""" + nom + """</a>');
"""
#fin prise donné par contact

    maps+="</script>"
#mapsend

    req.write(codeHTML("Localisation","""
<p><b>Localisation des contacts</b></p>
<br/>
""" + maps + lien("menu.py","Retour au menu")))
