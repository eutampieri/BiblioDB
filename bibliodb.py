#!/usr/bin/python2.7
# Versione 0.3-alpha
# Changelog:
# *Ora l'app utilizza Tkinter!
import json
from setDbName import setDbName
from deleteBook import deleteBook
from setBorrowTime import setBorrowTime
from datetime import date, datetime, time, timedelta
from Tkinter import *
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


def find(titolo):
    print"Titolo: \t"


def titToISBN(tit):
    Isbn = titleIsbn[tit]
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
    ISBNuse[pISBN] = state
    ISBNown[pISBN] = owner
    # INIZIO CODICE COPIATO DA
    # http://e-ware.org/blog/portare-avanti-o-indietro e-una-data-in-python/ e
    # riadattato
    data_prestito = datetime.today().strftime('%d/%m/%Y')
    data_fine = datetime.today() + timedelta(days=borrowTime)
    res = data_fine.strftime('%d/%m/%Y')
    ISBNborrowDate[pISBN] = data_prestito
    #    return res
    # Fine codice copiato
    print"Libro:\t" + ISBNTotit(pISBN).title() + "\nAutore: " + ISBNToAut(pISBN).title() + "\nISBN: \t" + pISBN + "\nPosizione:\t" + isbnPos[pISBN] + "\n" + 50 * '-' + '\n Stato:'
    if state == 0:
        print"Prestato a: " + owner
    elif state == 1:
        print"Reso da: " + owner
        ISBNown[pISBN] = "Biblioteca"
    print"RENDERE ENTRO:"
    print res
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


def manageISBN():
    # da implementare
    # print "Da implementare..."
    todoP = raw_input("Si preferisce usare l'ISBN o il titolo? ").lower()
    if todoP.lower() == 'isbn':
        isbn = raw_input("ISBN: ")
    else:
        titolo = raw_input("Titolo: ").lower()
        isbn = titToISBN(titolo)
    own = raw_input("Codice tessera: ")
    stato = input("Inserisci 0 per prestare il titolo, 1 per la resa. ")
    prestaISBN(isbn, stato, own)


def main():
    while True:
        print "Scrivi:\n* 's' per cambiare stato ad un volume;\n* 'a' per aggiungerne uno;\n* 'x' per generare un file TSV;\n* 'l' per ottenere una lista dei libri registrati;\n* 'i' per aprire il menu di impostazioni;"
        todoM = raw_input("* 'q' per uscire\n: ").lower()
        if todoM == 's':
            manageISBN()
        elif todoM.lower() == 'l':
            lista()
        elif todoM.lower() == 'x':
            tsvExport(nomeFile)
        elif todoM.lower() == 'q':
            break
        elif todoM.lower() == 'a':
            add()
        elif todoM.lower() == 'i':
            iInput = raw_input(
                "Scrivi 'e' per eliminare un libro, 'f' per cambiare il nome del file TSV o 'g' per cambiare il numero di giorni dei prestiti.").lower()
            if iInput == 'e':
                deleteBook()
            elif iInput == 'f':
                setDbName()
            else:
                print "ERRORE"
        else:
            print"ERRORE"


def lista():
    for isbn, num in isbnPos.items():
        print isbn + ":\t" + ISBNTotit(isbn).title() + ", " + ISBNToAut(isbn).title() + "\t" + num.upper()


def tsvExport(fileName):
    nome = (fileName.title()) + ".tsv"
    export = open(nome, 'w')
    export.write("ISBN o Codice\tTitolo\tAutore\tPosizione\n")
    for isbn, num in isbnPos.items():
        export.write(
            isbn +
            "\t" +
            ISBNTotit(isbn).title() +
            "\t" +
            ISBNToAut(isbn).title() +
            "\t" +
            num.upper() +
            "\n")
    export.close()
main()
class MiaApp:
  def __init__(self, genitore):
    self.mioGenitore = genitore  ### (7) ricorda: il genitore e` radice
    self.mioContenitore1 = Frame(genitore)
    self.mioContenitore1.pack()

    self.pulsante1 = Button(self.mioContenitore1)
    self.pulsante1.configure(text = "Conferma")
    self.pulsante1.bind("<Button-1>", self.pulsante1Premuto) ### (1)
    self.pulsante2 = Button(self.mioContenitore1)
    self.pulsante2.configure(text = "Annulla")   
    self.pulsante2.bind("<Button-1>", self.pulsante2Premuto) ### (2)
    self.pulsante3 = Button(self.mioContenitore1)
    self.pulsante3.configure(text = "Annulla")   
    self.pulsante3.bind("<Button-1>", self.pulsante2Premuto) ### (2)
    self.pulsante4 = Button(self.mioContenitore1)
    self.pulsante4.configure(text = "Annulla")   
    self.pulsante4.bind("<Button-1>", self.pulsante2Premuto) ### (2)
    self.pulsante5 = Button(self.mioContenitore1)
    self.pulsante5.configure(text = "Annulla")   
    self.pulsante5.bind("<Button-1>", self.pulsante2Premuto) ### (2)
    self.pulsante6 = Button(self.mioContenitore1)
    self.pulsante6.configure(text = "Annulla")   
    self.pulsante6.bind("<Button-1>", self.pulsante2Premuto) ### (2)
    self.pulsante1.pack()
    self.pulsante2.pack()
    self.pulsante3.pack()
    self.pulsante4.pack()
    self.pulsante5.pack()
                
  def pulsante1Premuto(self, evento):           ### (3)
    if self.pulsante1["background"] == "green": ### (4)
      self.pulsante1["background"] = "yellow"
    else:
      self.pulsante1["background"] = "green"
        
  def pulsante2Premuto(self, evento):  ### (5)
    self.mioGenitore.destroy()         ### (6)

                
radice = Tk()
miaApp = MiaApp(radice)
radice.mainloop()
