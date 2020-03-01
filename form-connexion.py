#!/usr/bin/python
# -*- coding: utf-8 -*-

import mod_python
import fonctions

def index(req):
	req.content_type="text/html"
	req.write(fonctions.codeHTML("Page de connexion","""
<h2>Veuillez vous connectez pour accéder à nos services.</h2>
<form method="POST" action="connexion.py">
    <table>
        <tr>
            <td>Login</td>
            <td><input type="text" name="login"/></td>
            <td></td>
        </tr>
        <tr>
            <td>Mot de passe</td>
            <td><input type="password" name="password"/></td>
            <td><input type="submit" value="Valider"/></td>
        </tr>
    </table>
</form>
"""))
