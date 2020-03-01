#!/usr/bin/python
# -*- coding: utf-8 -*-

#Le code de retour HTTP quand le serveur effectue une redirection est le 302.
#Le client est alors redirigé vers le formulaire de connexion.

from mod_python import Session, util
import fonctions

def index(req):
    req.content_type="text/html"
    sess = Session.Session(req)
    sess.delete()
    util.redirect(req, "form-connexion.py")
