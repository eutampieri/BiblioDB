#!/usr/bin/python2.7
import pickle
from setDbName import setDbName
from deleteBook import deleteBook
ISBNuse={}
#Dizionario che contiene le informazioni sullo stato dell'ISBN
isbnPos={}
#Dizionario contenente l'ISBN in relazione alla posizione del volume
titleIsbn={}
#Dizionario contenente il titolo in relazione all'ISBN
isbnTitle={}
#Dizionario contenente l'autore in relazione all'ISBN
isbnAuthor={}
#Dizionario contenente il proprietario in relazione all'ISBN
ISBNown={}
nomeFile="db_libri"
try:
    o=open('bibliodb.pickle','r')
except IOError:
    o=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    o.close()
else:
    o.close
finally:
    with open('bibliodb.pickle','r') as o:
                    ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor,nomeFile=pickle.load(o)
                    o.close
def add():
    titolo=raw_input("Titolo: ").lower()
    autore=raw_input("Autore: ").lower()
    isbn=raw_input("ISBN o ID volume: ")
    pos=raw_input("La posizione: ")
    isbnPos[isbn]=pos
    titleIsbn[titolo]= isbn
    isbnTitle[isbn]= titolo
    isbnAuthor[isbn]=autore
    o=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    o.close()
    pass
def find(titolo):
    print"Titolo: \t"
def titToISBN(tit):
    Isbn=titleIsbn[tit]
    return Isbn
    pass
def ISBNTotit(tISBN):
    titP=isbnTitle[tISBN]
    return titP
    pass
def ISBNToAut(aISBN):
    autP=isbnAuthor[aISBN]
    return autP
def prestaISBN(pISBN,state):
    ISBNuse[pISBN]=state
    o=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    o.close()
    print"Libro:\t\t"+ISBNTotit(pISBN)+"\n+Posizione:\t"+isbnPos[pISBN]+"\nStato:\t\t"
    if state==0:
        print"Prestato"
    elif state==1:
        print"Reso"
def manageISBN():
    #da implementare
    print "Da implementare..."
    todoP=raw_input("Si preferisce usare l'ISBN o il titolo? ").lower()
    if todoP.lower()=='isbn':
        isbn=raw_input("ISBN: ")
    else:
        titolo=raw_input("Titolo: ").lower()
        isbn=titToISBN(titolo)
    prestaISBN(isbn,0)
def main():
    while 1:
        print "Scrivi:\n* 's' per cambiare stato ad un volume;\n* 'a' per aggiungerne uno;\n* 'x' per generare un file TSV;\n* 'l' per ottenere una lista dei libri registrati;\n* 'i' per aprire il menu di impostazioni;"
        todoM=raw_input("* 'q' per uscire\n: ").lower()
        if todoM=='s':
            manageISBN()
        elif todoM.lower()=='l':
            lista()
        elif todoM.lower()=='x':
            tsvExport(nomeFile)
        elif todoM.lower()=='q':
            break
        elif todoM.lower()=='a':
            add()
        elif todoM.lower()=='i':
            iInput=raw_input("Scrivi 'e' per eliminare un libro, 'f' per cambiare il nome del file TSV").lower()
            if iInput=='e':
                deleteBook()
            elif iInput=='f':
                setDbName()
            else:
                print "ERRORE"
        else:
            print"ERRORE"
def lista():
    for isbn, num in isbnPos.items():
        print isbn+":\t"+ISBNTotit(isbn).title()+", "+ISBNToAut(isbn).title()+"\t"+num.upper()
#while True:
#    add()
def tsvExport(fileName):
    nome=(fileName.title())+".tsv"
    export=open(nome,'w')
    export.write("ISBN o Codice\tTitolo\tAutore\tPosizione\n")
    for isbn, num in isbnPos.items():
        export.write (isbn+"\t"+ISBNTotit(isbn).title()+"\t"+ISBNToAut(isbn).title()+"\t"+num.upper()+"\n")
    export.close()
main()
