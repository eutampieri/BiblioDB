from flask import *
import json
ISBNuse = {}
# Dizionario che contiene le informazioni sullo stato dell'ISBN
isbnPos = {}
# Dizionario contenente l'ISBN in relazione alla posizione del volume
titleIsbn = {}
# Dizionario contenente il titolo in relazione all'ISBN
isbnTitle = {}
# Dizionario contenente l'autore in relazione all'ISBN
isbnAuthor = {}
# Dizionario contenente il proprietario in relazione all'ISBN
ISBNown = {}
ISBNborrowDate = {}
nomeFile = "db_libri"
borrowTime = 30
try:
	o = open('bibliodb.json', 'r')
except IOError:
	o = open('bibliodb.json', 'w')
	json.dump(
		(ISBNuse,
		 isbnPos,
		 titleIsbn,
		 isbnTitle,
		 isbnAuthor,
		 nomeFile,
		 ISBNown,
		 borrowTime,
		 ISBNborrowDate),
		o)
	o.close()
else:
	o.close
finally:
	with open('bibliodb.json', 'r') as o:
		ISBNuse, isbnPos, titleIsbn, isbnTitle, isbnAuthor, nomeFile, ISBNown, borrowTime, ISBNborrowDate = json.load(
			o)
		o.close


def add():
	titolo = raw_input("Titolo: ").lower()
	autore = raw_input("Autore: ").lower()
	isbn = raw_input("ISBN o ID volume: ")
	pos = raw_input("La posizione: ")
	isbnPos[isbn] = pos
	titleIsbn[titolo] = isbn
	isbnTitle[isbn] = titolo
	isbnAuthor[isbn] = autore
	ISBNown[isbn]="Biblioteca"
	o = open('bibliodb.json', 'w')
	json.dump(
		(ISBNuse,
		 isbnPos,
		 titleIsbn,
		 isbnTitle,
		 isbnAuthor,
		 nomeFile,
		 ISBNown,
		 borrowTime,
		 ISBNborrowDate),
		o)
	o.close()
	pass

def find(mode,string):
	if mode==1:
		isbnCode=string
	elif mode==2:
		isbnCode=titToISBN(string.lower())
	pos=isbnPos[isbnCode].upper()
	titoloOpera=ISBNTotit(isbnCode).title()
	toReturn="----------------------------------\nTitolo:\t"+titoloOpera+"\nISBN:\t"+isbnCode+"\nAutore:\t"+ISBNToAut(isbnCode).title()+"\nPosizione:\t"+pos+"\n----------------------------------\n"
	return toReturn


def titToISBN(tit):
	try:
		Isbn = titleIsbn[tit]
	except KeyError:
	   Isbn=0
	return Isbn
	pass


def ISBNTotit(tISBN):
	titP = isbnTitle[tISBN]
	return titP
	pass


def ISBNToAut(aISBN):
	autP = isbnAuthor[aISBN]
	return autP


def prestaISBN(pISBN, state, owner):
	strPrestito=""
	#try:
	oldOwner=ISBNown[pISBN]
	ISBNuse[pISBN] = state
	ISBNown[pISBN] = owner
	data_prestito = datetime.today().strftime('%d/%m/%Y')
	data_fine = datetime.today() + timedelta(days=borrowTime)
	res = data_fine.strftime('%d/%m/%Y')
	ISBNborrowDate[pISBN] = data_prestito
	strPrestito=strPrestito+"Libro:\t" + ISBNTotit(pISBN).title() + "\nAutore: " + ISBNToAut(pISBN).title() + "\nISBN: \t" + pISBN + "\nPosizione:\t" + isbnPos[pISBN] + "\n" + 50 * '-' + '\n Stato:\n'
	if state == 0:
		strPrestito=strPrestito+"Prestato a: " + owner+'\n'
		strPrestito=strPrestito+"RENDERE ENTRO:\n"
		strPrestito=strPrestito+ res+'\n'
	elif state == 1:
		strPrestito=strPrestito+"Reso da: " + oldOwner+'\n'
		ISBNown[pISBN] = "Biblioteca"
		strPrestito=strPrestito+ "Prestato il: "+ISBNborrowDate[pISBN]+'\n'
	o = open('bibliodb.json', 'w')
	json.dump(
		(ISBNuse,
		 isbnPos,
		 titleIsbn,
		 isbnTitle,
		 isbnAuthor,
		 nomeFile,
		 ISBNown,
		 borrowTime,
		 ISBNborrowDate),
		o)
	o.close()
	#except KeyError:
	#   print"ERRORE"
	return strPrestito
def lista():
    list=""
    for isbn, num in isbnPos.items():
        list=list+isbn + ":\t" + ISBNTotit(isbn).title() + ", " + ISBNToAut(isbn).title() + "\t" + num.upper()+"\n"
    return list
def tsvExport():
    export = ""
    export=export +"ISBN o Codice\tTitolo\tAutore\tPosizione\n"
    for isbn, num in isbnPos.items():
        try:
            export=export+isbn +"\t" +ISBNTotit(isbn).title() +"\t" +ISBNToAut(isbn).title() +"\t" +num.upper() +"\n"
        except UnicodeEncodeError:
            export=export+" \t \t \t \n"
    return export
app = Flask(__name__)

@app.route('/isbninfo/titolo/<isbn>')
def isbnTitolo(isbn):
	resp=Response(response=ISBNTotit(str(isbn).upper()).title(), status=200,mimetype="text/plain")
	return resp
@app.route('/isbninfo/scheda/<titolo>')
def scheda(titolo):
	resp=""
	try:
		isbn=titToISBN(titolo.lower())
	except KeyError:
		resp=Response(response="Errore: Controlla il titolo",status=200,mimetype="text/plain")
	else:
		resp=Response(response="Titolo: "+ISBNTotit(str(isbn).upper()).title()+"\nAutore: "+ISBNToAut(str(isbn).upper()).title()+"\nPosizione: "+isbnPos[isbn.upper()].upper()+"\nISBN: "+isbn.upper(), status=200,mimetype="text/plain")
	finally:
		return resp
@app.route('/isbninfo/isbn/<titolo>')
def TitoloIsbn(titolo):
	resp=Response(response=IStitToISBN(str(titolo).lower()).title(), status=200,mimetype="text/plain")
	return resp
@app.route('/isbninfo/posizione/<isbn>')
def isbnPosizione(isbn):
	resp = Response(response=isbnPos[str(isbn).upper()].upper(), status=200,mimetype="text/plain")
	return resp
@app.route('/isbninfo/autore/<isbn>')
def isbnAutore(isbn):
	resp = Response(response=ISBNToAut(str(isbn).upper()).title(), status=200,mimetype="text/plain")
	return resp
@app.route('/lista')
def listaTitoli():
	resp = Response(response=lista(), status=200,mimetype="text/plain")
	return resp
@app.route('/json')
def jsonGetter():
	json=open('bibliodb.json','r')
	str=""
	for lines in json:
		str=str+lines
	resp = Response(response=str, status=200,mimetype="application/json")
	return resp
@app.route('/tsv')
def tsvGetter():
	tsv=tsvExport()
	resp = Response(response=tsv, status=200,mimetype="text/tab-separeted-values")
	return resp
@app.route('/')
def Welcome():
	return"<html><head><title>BiblioDB API</title></head><body><h1>Benvenuti in BiblioDB!</h1><br><p>Per utilizzare l'api e' necessario modificare l'URL.</p></body></html"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
@app.route('/update')
def update():
	ISBNuse = {}
	# Dizionario che contiene le informazioni sullo stato dell'ISBN
	isbnPos = {}
	# Dizionario contenente l'ISBN in relazione alla posizione del volume
	titleIsbn = {}
	# Dizionario contenente il titolo in relazione all'ISBN
	isbnTitle = {}
	# Dizionario contenente l'autore in relazione all'ISBN
	isbnAuthor = {}
	# Dizionario contenente il proprietario in relazione all'ISBN
	ISBNown = {}
	ISBNborrowDate = {}
	nomeFile = "db_libri"
	borrowTime = 30
	try:
		o = open('bibliodb.json', 'r')
	except IOError:
		o = open('bibliodb.json', 'w')
		json.dump(
			(ISBNuse,
			 isbnPos,
			 titleIsbn,
			 isbnTitle,
			 isbnAuthor,
			 nomeFile,
			 ISBNown,
			 borrowTime,
			 ISBNborrowDate),
			o)
		o.close()
	else:
		o.close
	finally:
		with open('bibliodb.json', 'r') as o:
			ISBNuse, isbnPos, titleIsbn, isbnTitle, isbnAuthor, nomeFile, ISBNown, borrowTime, ISBNborrowDate = json.load(
				o)
			o.close
