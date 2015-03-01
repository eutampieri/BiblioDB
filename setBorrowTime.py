import json
def setBorrowTime():
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
    borrowTime=30
    try:
    	o=open('bibliodb.json')
    except IOError:
    	o=open('bibliodb.json','w')
    	json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowTime),o)
    	o.close()
    else:
    	o.close
    finally:
        with open('bibliodb.json','r') as o:
                        ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor,fileName,ISBNown,borrowTime=json.load(o)
                        o.close
    borrowTime=input("Numero di giorni prestito libri: ")
    s=open('bibliodb.json','w')
    json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowTime),s)
    s.close()
    print "Il numero giorni e' stato aggiornato"