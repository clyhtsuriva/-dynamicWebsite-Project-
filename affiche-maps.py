#!/usr/bin/python
#coding: utf-8
#EXO 21 : EN TRAVAUX

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
	req.content_type="text/html"

	sess = Session.Session(req)
	redirectionSiNonConnecte(req,sess)
	id_util=sess["id_util"]
	nom=req.form["nom"]
	
	conn = connexionBD()
    	cur = conn.cursor()

    	sql = "select * from contact where id_util={} and latitude is not null and longitude is not null and nom like '%{}%';".format(id_util, nom)
    	cur.execute(sql)
    	conn.commit()
    	data = cur.fetchall()
    	conn.close()

	for i in range(len(data)):
        	lat=str(data[i][5])
	        lon=str(data[i][6])
	        id_contact=str(data[i][0])
	        nom=str(data[i][1])
		maps=""
	        
		contact+="""
var m = L.marker({lat: """ + lat + """, lon: """ + lon + """});
        m.addTo(map);
        m.bindPopup('<a href="fiche.py?id_contact=""" + id_contact + """">""" + nom + """</a>');
"""

	req.write("""
<script>
        var map = L.map("carte");
        map.setView({lat: 0 , lon: 0}, 1);
        url="https://{s}.tile.openstreetmap.org" + "/{z}/{x}/{y}.png";
        var layer = L.tileLayer(url);
        layer.addTo(map);
""" + contact)
