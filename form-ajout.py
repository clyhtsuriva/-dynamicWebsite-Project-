#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
import fonctions

def index(req):
    req.content_type="text/html"

    sess = Session.Session(req)
    fonctions.redirectionSiNonConnecte(req,sess)

    req.write(fonctions.codeHTML("Ajout d'un contact","""
<p><b>Ajout d'un contact</b></p>
<form method="POST" action="ajout.py" onsubmit="return isItGood()">
    <table>
        <tr>
            <td>Nom</td>
            <td><input type="text" name="nom" id="nom"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Adresse</td>
            <td><input type="text" name="adresse"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><input type="text" name="email" id="email"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Téléphone</td>
            <td><input type="text" name="telephone" id="telephone"/></td>
            <td><input type="submit" value="Valider" id="submit"></td>
        </tr>
    </table>
</form>
""" + fonctions.lien("menu.py","Retour au menu principal") + """
<script src="form-ajout.js"></script>
"""))
