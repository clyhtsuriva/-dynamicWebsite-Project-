#!/usr/bin/python
# -*- coding: utf-8 -*-

import mod_python
from fonctions import lien, redirectionSiNonConnecte, codeHTML
from mod_python import Session

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req)
    redirectionSiNonConnecte(req,sess)
    
    req.write(codeHTML("Menu principal","""
<p><b>Menu principal</b><br/>
Vous êtes connecté en tant que <b>""" + sess["login"] + """</b>
</p>
<ul>
    <li>""" + lien("form-ajout.py","Ajout d'un contact") +  """</li>
    <li>""" + lien("liste.py","Liste des contacts") + """</li>
    <li>""" + lien("localisation.py","Localisation des contacts") + """</li>
    <li>""" + lien("form-ajout-util.py","Ajout d'un utilisateur") + """</li>
    <li>""" + lien("deconnexion.py","Déconnexion") + """</li>
</ul>
"""))
