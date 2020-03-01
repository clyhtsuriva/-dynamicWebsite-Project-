#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from fonctions import redirectionSiNonConnecte, lien, codeHTML

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req)
    redirectionSiNonConnecte(req,sess)

    req.write(codeHTML("Liste des contacts","""
    <p><b>Liste des contacts</b></p>
    <b>Rechercher un nom :</b>
    <input type="text" id="nom" onkeyup="cherche()"/><br/>
    <div id="liste"></div>
    """ + lien("menu.py","Retour au menu") +"""
<script src="liste.js"></script>
"""))
