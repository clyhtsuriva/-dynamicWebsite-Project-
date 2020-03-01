#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML, connexionBD

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req) #recup session
    redirectionSiNonConnecte(req,sess) #redirige si la session est nouvelle
    id_util=sess["id_util"] #recup l'id_util

#start sql check que l'util est root
    conn = connexionBD()
    cur = conn.cursor()
    sql = "select login from util where util.id_util={} and util.login='{}';".format(id_util, 'root')
    cur.execute(sql)
    conn.commit()
    data = cur.fetchall()
    if not data:
	 req.write(codeHTML("Erreur !", """
<h3><g>Seul l'utilisateur root a le droit d'ajouter un utilisateur.</g></h3>
""" + lien('menu.py',"Retour au menu")))
#end sql check util root

    else:
	req.write(codeHTML("Ajout d'un utilisateur","""
<p><b>Ajout d'un utilisateur</b></p>
<form method="POST" action="ajout-util.py" onsubmit="return isItGood()">
    <table>
        <tr>
            <td>Login</td>
            <td><input type="text" name="login" id="login" onkeyup="alreadyUsed()"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Mot de passe</td>
            <td><input type="password" name="motdepasse" id="motdepasse"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Confirmation du mot de passe</td>
            <td><input type="password" name="conf" id="conf"/></td>
            <td></td>
        </tr>
    </table>
    <div id="used"></div>
</form>
""" + lien("menu.py","Retour au menu principal") + """
<script src="form-ajout-util.js"></script>
"""))
