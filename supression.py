#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session, util
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req)
    redirectionSiNonConnecte(req,sess)
    id_util=sess["id_util"]
    id_contact=req.form["id_contact"]
    conn = connexionBD()
    cur = conn.cursor()

    sql = "select * from contact where id_contact={} and id_util={};".format(id_contact, id_util)
    cur.execute(sql)
    conn.commit()
    data = cur.fetchall()
    

    if not data:
        req.write(codeHTML("Erreur !", """
<p>Ce contact ne vous appartient pas.</p>
""" + lien('menu.py',"Retour au menu")))
	conn.close()
    else:
	sql = "delete from contact where id_contact={};".format(id_contact)
	cur.execute(sql)
	conn.commit()
	conn.close()
	util.redirect(req, "liste.py")
