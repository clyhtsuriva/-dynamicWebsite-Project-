#!/usr/bin/python
# -*- coding: utf-8 -*-

import mod_python
import fonctions
import psycopg2
from mod_python import Session

def index(req):
        req.content_type="text/html"
        
        sess = Session.Session(req)
         
        login=req.form['login']
        password=req.form['password']

	conn=fonctions.connexionBD()
	cur = conn.cursor()
	
        sql="select * from util where login=%s and mdp =%s;"
	cur.execute(sql, (login, password, ))
        data = cur.fetchall()
	           
        if not data:
            sess.delete()
            req.write(fonctions.codeHTML("Erreur !","""<h3>Identifiants invalides</h3>""" + fonctions.lien('form-connexion.py',"Retour à la page de connexion")))
            
        else:
            id_util=data[0]
            sess["login"]=login
            sess["id_util"]=id_util[0]
            sess.save()
            req.write(fonctions.codeHTML("Connexion","""<h3>Identifiants valides</h3>""" + fonctions.lien('menu.py',"Menu du site")))
