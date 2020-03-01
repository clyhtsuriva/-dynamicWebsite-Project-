#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# fonction a utiliser :
# - geocodageIUTV si vous êtes à l'IUT (utilisation nécessaire du proxy)
# - geocodage sinon

import urllib
import urllib2
from xml.dom import minidom

def geocodageIUTV(adresse):
    try:
        proxy = urllib2.ProxyHandler({'https': '192.168.1.246:3128'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        reponse = urllib2.urlopen(getURL(adresse))
        return analyseResultat(reponse)
    except:
        return None

def geocodage(adresse):
    try:
        url = "http://nominatim.openstreetmap.org/search?format=xml&q=" + \
              urllib.quote_plus(adresse)
        reponse = urllib2.urlopen(getURL(adresse))
        return analyseResultat(reponse)
    except:
        return None

def getURL(adresse):
    return "https://nominatim.openstreetmap.org/search?format=xml&q=" + urllib.quote_plus(adresse)

def analyseResultat(reponse):
    xml = reponse.read()
    doc = minidom.parseString(xml)
    place = doc.getElementsByTagName("place")[0]
    lat = place.attributes["lat"].value
    lon = place.attributes["lon"].value
    return lat, lon
    
#  fonction de test (ne pas utiliser dans votre code)
def index(req):
    req.content_type = "text/html"
    pos = geocodageIUTV(req.form["adresse"])
    if pos == None:
        req.write("Adresse non trouvée")
    else:
        lat, lon = pos
        req.write("Latitude = " + str(lat) + ", Longitude = " + str(lon))
