#!/usr/bin/python
# -*- coding: utf-8 -*-

import mod_python
import fonctions

def index(req):
	req.content_type="text/html"
	req.write(fonctions.codeHTML("Mon premier script","Voici mon premier script de web dynamique!"))


