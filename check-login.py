#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
	req.content_type="text/html"

	sess = Session.Session(req)
	redirectionSiNonConnecte(req,sess)
	id_util=sess["id_util"]
	login=req.form["login"]
	conn = connexionBD()
	cur = conn.cursor()

	sql = "select login from util where util.login='{}';".format(login)
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        conn.close()

	if not data:
		req.write("""<input type="submit" value="Valider" id="submit">""")
	else :
		req.write ("""<b>Erreur : Ce login est déjà utilisé par un autre utilisateur</b>""")
