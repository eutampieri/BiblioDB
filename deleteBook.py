import pickle
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
    try:
    	o=open('bibliodb.pickle')
    except IOError:
    	o=open('bibliodb.pickle','w')
    	pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor),o)
    	o.close()
    else:
    	o.close
    finally:
        with open('bibliodb.pickle','r') as o:
                        ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor=pickle.load(o)
                        o.close
    def ISBNTotit(tISBN):
        titP=isbnTitle[tISBN]
        return titP
        pass
    scheda=raw_input("ISBN da eliminare: ")
    #ISBNuse e' riservato per utilizzi successivi. Non decommentare
    #ISBNuse.pop(scheda)
    isbnPos.pop(scheda)
    titleIsbn.pop(ISBNTotit(scheda))
    isbnAuthor.pop(scheda)
    s=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor),s)
    s.close()
    print 'La voce',scheda,'e stata eliminata correttamente!'
