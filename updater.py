import urllib2
import platform
from os import system
from uuid import uuid4
import json
def update():
	try:
		o = open('uuid', 'r')
	except IOError:
		o = open('uuid', 'w')
		o.write(str(uuid4()))
		o.close()
	else:
		o.close()
	finally:
		o = open('uuid', 'r')
		Uuid=o.read()
		o.close()
	url="https://raw.githubusercontent.com/eutampieri/BiblioDB/master/version"
	versionfile=open('version','r')
	actualVersion=int(versionfile.read())
	versionfile.close()
	try:
		gesturl="http://serverseutampieri.ddns.net:4049/provision/"+str(Uuid)+"/Python-main-updater/"+str(actualVersion)
		sendGestionale = urllib2.urlopen(gesturl)
		Gestionale=sendGestionale.read()
	except:
		return "Non riesco a connettermi alla telegestione a causa di un Errore Internet"
	try:
		version = urllib2.urlopen(url)
		gitVersion=int(version.read())
	except:
		return "Non riesco a ottenere la lista delle versioni a causa di un Errore Internet"
	else:
		if gitVersion>actualVersion:
			if platform.system()=="Linux" or platform.system()=="Darwin":
				system("git pull origin master")
				exit()
			else:
				return "Visitare la pagina web https://github.com/eutampieri/BiblioDB/releases"
		else:
			return "Aggiornato!"
def Cupdate():
	update()
