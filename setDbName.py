import json
def setDbName():
    ISBNuse={}
    #Dizionario che contiene le informazioni sullo stato dell'ISBN
    isbnPos={}
    #Dizionario contenente l'ISBN in relazione alla posizione del volume
    titleIsbn={}
    #Dizionario contenente il titolo in relazione all'ISBN
    isbnTitle={}
    #Dizionario contenente l'autore in relazione all'ISBN
    isbnAuthor={}
    fileName=""
    borrowtime=30
    try:
    	o=open('bibliodb.json')
    except IOError:
    	o=open('bibliodb.json','w')
    	json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime),o)
    	o.close()
    else:
    	o.close
    finally:
        with open('bibliodb.json','r') as o:
                        ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime=json.load(o)
                        o.close
    fileName=raw_input("Nome del file DB da esportare: ")
    s=open('bibliodb.json','w')
    json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime),s)
    s.close()
    print "Il nome del file e' stato aggiornato"