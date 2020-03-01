#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import mod_python

def codeHTML(titre, corps):
    content=("""<!DOCTYPE html>
<html>
	<head>
		<title>""" + titre + """</title>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>""" + corps + """</body>
</html>""")

    return content

def connexionBD():
#    connexion=psycopg2.connect ("host='aquabdd' dbname='etudiants' user='11802407' password='153067690FG'")
    connexion=psycopg2.connect ("host='localhost' dbname='devweb' user='devweb' password='123456'")
    return connexion

def lien(url, texte):
    content=("""<a href=" """ + url + """ ">""" + texte + """</a>""")
    return content

def redirectionSiNonConnecte(req,sess):
    if sess.is_new():
        mod_python.util.redirect(req, "form-connexion.py")
