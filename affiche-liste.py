#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    sql = "select id_contact, nom from contact where id_util={} and nom like '%{}%';".format(id_util, nom)
    cur.execute(sql)
    conn.commit()
    data = cur.fetchall()
    conn.close()

    for i in data:
	req.write("""<ul><li>""" + lien('fiche.py?id_contact=' + str(i[0]), str(i[1])) + """</li></ul>""")
