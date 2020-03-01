#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req) #recup session
    redirectionSiNonConnecte(req,sess) #redirige si la session est nouvelle
    id_util=sess["id_util"] #recup l'id_util

    login=req.form['login']
    mdp=req.form['motdepasse']

    conn=connexionBD()
    cur = conn.cursor()
    sql="insert into util (login,mdp) values (%s,%s);"
    cur.execute(sql, (login, mdp, ))
    conn.commit()
    conn.close()

    req.write(codeHTML("","""
<p><b>Nouvel utilisateur</b></p>
<p>""" + login + """ a bien été ajouté</p>
""" + lien('menu.py',"Retour au menu principal")))

