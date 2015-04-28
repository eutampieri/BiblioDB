import urllib2
import platform
from os import system
def update():
	url="https://raw.githubusercontent.com/eutampieri/BiblioDB/master/version"
	actualVersion=110
	try:
		version = urllib2.urlopen(url)
		gitVersion=int(version.read())
	except:
		return "Non riesco a ottenere\nla lista delle versioni\na causa di un\nErrore Internet"
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
	url="https://raw.githubusercontent.com/eutampieri/BiblioDB/master/version"
	actualVersion=110
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