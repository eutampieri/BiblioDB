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
    fileName="libri"
    borrowtime=30
    nerrori=0
    wrongisbn=""
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
                        o.close
    try:
        for isbn, num in isbnTitle.items():
            wrongisbn=isbn
            isbnTitle[isbn]=num.lower()
            ISBNown[isbn]="Biblioteca"
            ISBNuse[isbn]=1
            isbnAuthor[isbn]=isbnAuthor[isbn].lower()
            isbnPos[isbn]=isbnPos[isbn].upper()
    except KeyError:
        nerrori=nerrori+1
        print "ERRORE N "+str(nerrori)
        print wrongisbn
        try:
            print isbnTitle[wrongisbn]
        except KeyError:
            print "Non esiste il titolo!"
    s=open('bibliodb.json','w')
    json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,fileName,ISBNown,borrowtime,ISBNborrowDate),s)
    s.close()
    print 'DB corretto!'

FixDB()