import json
def FixDB():
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
    ISBNborrowDate = {}
    ISBNown = {}
    try:
    	o=open('bibliodb.json')
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
    else:
    	o.close
    finally:
        with open('bibliodb.json','r') as o:
                        ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate=json.load(o)
                        o.close
    def ISBNTotit(tISBN):
        titP=isbnTitle[tISBN]
        return titP
        pass
    for isbn, num in isbnTitle.items():
        ISBNown[isbn]="Biblioteca"
    for isbn, num in isbnTitle.items():
        ISBNuse[isbn]=1
    s=open('bibliodb.json','w')
    json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate),s)
    s.close()
    print 'DB corretto!'
FixDB()