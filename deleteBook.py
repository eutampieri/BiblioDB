import json
def ISBNTotit(tISBN):
	titP=isbnTitle[tISBN]
	return titP
	pass
def deleteBook():
	ISBNuse={}
	#Dizionario che contiene le informazioni sullo stato dell'ISBN
	isbnPos={}
	#Dizionario contenente l'ISBN in relazione alla posizione del volume
	titleIsbn={}
	#Dizionario contenente il titolo in relazione all'ISBN
	isbnTitle={}
	#Dizionario contenente l'autore in relazione all'ISBN
	isbnAuthor={}
	ISBNown={}
	fileName=""
	borrowtime=30
	ISBNborrowDate = {}
	try:
		o=open('bibliodb.json')
	except IOError:
		o=open('bibliodb.json','w')
		json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate),o)
		o.close()
	else:
		o.close
	finally:
		with open('bibliodb.json','r') as o:
			ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate=json.load(o)
			o.close()
	scheda=raw_input("ISBN da eliminare: ")
	#ISBNuse e' riservato per utilizzi successivi. Non decommentare
	ISBNuse.pop(scheda)
	isbnPos.pop(scheda)
	titleIsbn.pop(ISBNTotit(scheda))
	isbnAuthor.pop(scheda)
	ISBNown.pop(scheda)
	ISBNborrowDate.pop(scheda)
	s=open('bibliodb.json','w')
	json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate),s)
	s.close()
	print 'La voce',scheda,'e stata eliminata correttamente!'