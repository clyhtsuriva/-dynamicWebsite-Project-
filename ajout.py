#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
import fonctions
import psycopg2
import geocodage

def index(req):
        req.content_type="text/html"
        sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req,sess)
        
	nom=req.form['nom']
        adresse=req.form['adresse']
        email=req.form['email']
        telephone=req.form['telephone']
        id_util=sess["id_util"]

        conn=fonctions.connexionBD()
        cur = conn.cursor()
#debut geocodage
#	geo=geocodage.geocodageIUTV(adresse) #decommentez pour utilisation IUT
	geo=geocodage.geocodage(adresse)    #decommentez pour utilisation home
	if not geo:
		lat=None
		lon=None
	else : 
		lat=geo[0]
		lon=geo[1]
#fin geocodage
        sql="insert into contact (nom,email,tel,adresse,latitude,longitude,id_util) values (%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(sql, (nom, email, telephone, adresse, lat, lon, id_util, ))
        conn.commit()
        conn.close()

        req.write(fonctions.codeHTML("Nouveau contact","""
<p><b>Nouveau contact</b></p>
<p>""" + nom + """ a bien été ajouté à vos contacts</p>
""" + fonctions.lien('menu.py',"Retour au menu principal")))
