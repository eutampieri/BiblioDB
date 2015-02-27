#!/usr/bin/python2.7
import pickle
from setDbName import setDbName
from deleteBook import deleteBook
ISBNuse={}
#Dizionario che contiene le informazioni sullo stato dell'ISBN
isbnPos={}
#Dizionario contenente l'ISBN in relazione alPlacing del volume
titleIsbn={}
#Dizionario contenente il titolo in relazione all'ISBN
isbnTitle={}
#Dizionario contenente l'Author in relazione all'ISBN
isbnAuthor={}
#Dizionario contenente il proprietario in relazione all'ISBN
ISBNown={}
nomeFile="db_libri"
try:
    or=open('bibliodb.pickle','r')
except IOError:
    or=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    or.close()
else:
    or.close
finally:
    with orpen('bibliodb.pickle','r') as or:
                    ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor,nomeFile=pickle.load(o)
                    or.close
def add():
    titolo=raw_input("Title: ").lower()
    Author=raw_input("Author: ").lower()
    isbn=raw_input("ISBN or volume ID: ")
    pos=raw_input("Placing: ")
    isbnPos[isbn]=pos
    titleIsbn[titolo]= isbn
    isbnTitle[isbn]= titolo
    isbnAuthor[isbn]=Author
    or=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    or.close()
    pass
def find(titolo):
    print"Title: \t"
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
    or=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown),o)
    or.close()
    print"Book:\t\t"+ISBNTotit(pISBN)+"\n+Placing:\t"+isbnPos[pISBN]+"\nState:\t\t"
    if state==0:
        print"Borrowed"
    elif state==1:
        print"Reso"
def manageISBN():
    #da implementare
    print "Da implementare..."
    todoP=raw_input("Si preferisce usare l'ISBN or il titolo? ").lower()
    if todoP.lower()=='isbn':
        isbn=raw_input("ISBN: ")
    else:
        titolo=raw_input("Title: ").lower()
        isbn=titToISBN(titolo)
    prestaISBN(isbn,0)
def main():
    while 1:
        print "Scrivi:\n* 's' per cambiare stato ad un volume;\n* 'a' per aggiungerne uno;\n* 'x' per generare un file TSV;\n* 'l' per orttenere una lista dei libri registrati;\n* 'i' per aprire il menu di impostazioni;"
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
            iInput=raw_input("Scrivi 'e' per eliminare un Book, 'f' per cambiare il nome del file TSV").lower()
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
    export.write("ISBN or ID\tTitolo\tAuthor\tPlacing\n")
    for isbn, num in isbnPos.items():
        export.write (isbn+"\t"+ISBNTotit(isbn).title()+"\t"+ISBNToAut(isbn).title()+"\t"+num.upper()+"\n")
    export.close()
main()
