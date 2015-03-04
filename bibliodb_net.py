#!/usr/bin/env python# Versione 0.3
# Changelog:
# *Ora l'app utilizza Tkinter!
# *Nuova grafica a frames
import urllib2
import json
from Tkinter import *
from ttk import *
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
    response = urllib2.urlopen('http://192.168.1.22:5000/json')
except urllib2.HTTPError:
    print "Errore Internet"
else:
    print "OK"
finally:
    response = urllib2.urlopen('http://192.168.1.22:5000/json')
    newJSON=response.read()
    ISBNuse, isbnPos, titleIsbn, isbnTitle, isbnAuthor, nomeFile, ISBNown, borrowTime, ISBNborrowDate = json.loads(newJSON)


def add():
    titolo = raw_input("Titolo: ").lower()
    autore = raw_input("Autore: ").lower()
    isbn = raw_input("ISBN o ID volume: ")
    pos = raw_input("La posizione: ")
    isbnPos[isbn] = pos
    titleIsbn[titolo] = isbn
    isbnTitle[isbn] = titolo
    isbnAuthor[isbn] = autore
    ISBNown[isbn] = "Biblioteca"
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


def GUIadd(titolo, autore, isbn, pos):
    isbnPos[isbn] = pos
    titleIsbn[titolo] = isbn
    isbnTitle[isbn] = titolo
    isbnAuthor[isbn] = autore
    ISBNown[isbn] = "Biblioteca"
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


def find(mode, string):
    if mode == 1:
        isbnCode = string
    elif mode == 2:
        isbnCode = titToISBN(string.lower())
    pos = isbnPos[isbnCode].upper()
    titoloOpera = ISBNTotit(isbnCode).title()
    toReturn = "----------------------------------\nTitolo:\t" + titoloOpera + "\nISBN:\t" + isbnCode + \
        "\nAutore:\t" + ISBNToAut(isbnCode).title() + "\nPosizione:\t" + pos + "\n----------------------------------\n"
    return toReturn


def titToISBN(tit):
    try:
        Isbn = titleIsbn[tit]
    except KeyError:
        Isbn = 0
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
    strPrestito = ""
    # try:
    oldOwner = ISBNown[pISBN]
    ISBNuse[pISBN] = state
    ISBNown[pISBN] = owner
    data_prestito = datetime.today().strftime('%d/%m/%Y')
    data_fine = datetime.today() + timedelta(days=borrowTime)
    res = data_fine.strftime('%d/%m/%Y')
    ISBNborrowDate[pISBN] = data_prestito
    strPrestito = strPrestito + "Libro:\t" + ISBNTotit(pISBN).title() + "\nAutore: " + ISBNToAut(
        pISBN).title() + "\nISBN: \t" + pISBN + "\nPosizione:\t" + isbnPos[pISBN] + "\n" + 50 * '-' + '\n Stato:\n'
    if state == 0:
        strPrestito = strPrestito + "Prestato a: " + owner + '\n'
        strPrestito = strPrestito + "RENDERE ENTRO:\n"
        strPrestito = strPrestito + res + '\n'
    elif state == 1:
        strPrestito = strPrestito + "Reso da: " + oldOwner + '\n'
        ISBNown[pISBN] = "Biblioteca"
        strPrestito = strPrestito + "Prestato il: " + \
            ISBNborrowDate[pISBN] + '\n'
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
    # except KeyError:
    #   print"ERRORE"
    return strPrestito


def manageISBN():
    todoP = raw_input("Si preferisce usare l'ISBN o il titolo? ").lower()
    if todoP.lower() == 'isbn':
        isbn = raw_input("ISBN: ")
    else:
        titolo = raw_input("Titolo: ").lower()
        isbn = titToISBN(titolo)
    own = raw_input("Codice tessera: ")
    stato = input("Inserisci 0 per prestare il titolo, 1 per la resa. ")
    print prestaISBN(isbn, stato, own)


def main():
    print "VERSIONE DI CONSULTAZIONE. NON E POSSIBILE APPORTARE MODIFICHE"
    while True:
        print "Scrivi:\n* 's' per cambiare stato ad un volume;\n* 'a' per aggiungerne uno;\n* 'x' per generare un file TSV;\n* 'l' per ottenere una lista dei libri registrati;\n* 'i' per aprire il menu di impostazioni;"
        todoM = raw_input("* 'q' per uscire\n: ").lower()
        if todoM == 's':
            manageISBN()
        elif todoM.lower() == 'l':
            print lista()
        elif todoM.lower() == 'x':
            tsvExport(nomeFile)
        elif todoM.lower() == 'q':
            break
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
    list = ""
    for isbn, num in isbnPos.items():
        list = list + isbn + ":\t" + \
            ISBNTotit(isbn).title() + ", " + ISBNToAut(isbn).title() + "\t" + num.upper() + "\n"
    return list


def tsvExport(fileName):
    nome = (fileName.title()) + ".tsv"
    export = open(nome, 'w')
    export.write("ISBN o Codice\tTitolo\tAutore\tPosizione\n")
    for isbn, num in isbnPos.items():
        try:
            export.write(
                isbn +
                "\t" +
                ISBNTotit(isbn).title() +
                "\t" +
                ISBNToAut(isbn).title() +
                "\t" +
                num.upper() +
                "\n")
        except UnicodeEncodeError:
            export.write(" \t \t \t \n")
    export.close()


def ISBNoTit(text, type):
    if type == 1:
        return text
    else:
        return titToISBN(text)


def GuiInfos():
    info = Tk()
    w = Label(
        info,
        text="BiblioDB 0.3\n--------------------\nMIT Licence\nBy Eugenio Tampieri",
        font=(
            "Helvetica",
            16),
        justify=CENTER)
    w.pack()
    info.mainloop()


def GUI():
    info=Tk()
    mainFrame=Frame(info)
    mainFrame.pack()
    Label(mainFrame,text="Versione di consultazione.\n Non e' possibile apportare modifiche.", font=("Helvetica",16),justify=CENTER).pack()
    info.mainloop()
    ###########################################
    # Finestra Generale
    ###########################################
    Finestra = Tk()
    ###########################################
    # Menu
    ###########################################
    barramenu = Menu(Finestra)
    barramenu.add_command(
        label="Esporta!",
        command=lambda: tsvExport(nomeFile))
    barramenu.add_command(label="?", command=lambda: GuiInfos())
    Finestra.title = "BiblioDB 0.3"
    Finestra.config(menu=barramenu)
    ###########################################
    # Schede
    ###########################################
    n = Notebook(Finestra)
    Frlista = Frame(n)  # second page
    Trova = Frame(n)
    n.add(Frlista, text='Lista Libri')
    n.add(Trova, text="Ricerca Libro")
    n.pack()
    ###########################################
    # Scheda Lista
    ###########################################
    scrollbar = Scrollbar(Frlista)
    scrollbar.pack(side=RIGHT, fill=Y)
    etiLisT = Label(Frlista, text="Premi il pulsante per aggiornare la lista")
    etiLisT.pack()
    listaLibri = Text(Frlista, wrap=WORD, yscrollcommand=scrollbar.set)
    listaLibri.pack()
    scrollbar.config(command=listaLibri.yview)
    Button(
        Frlista,
        command=lambda: listaLibri.insert(
            INSERT,
            lista()),
        text="Aggiorna").pack()
    ###########################################
    # Scheda Ricerca
    ###########################################
    modo = IntVar()
    Radiobutton(Trova, text="ISBN", variable=modo, value=1).pack(anchor=W)
    Radiobutton(Trova, text="Titolo", variable=modo, value=2).pack(anchor=W)
    sL = Label(Trova, text="ISBN o Titolo:")
    sL.pack()
    s = Entry(Trova)
    s.pack()
    s.insert(0, "ISBN o Titolo")
    Button(
        Trova,
        command=lambda: outputPre.insert(
            INSERT,
            find(
                modo.get(),
                s.get())),
        text="Cerca").pack()
    scrollbar = Scrollbar(Trova)
    scrollbar.pack(side=RIGHT, fill=Y)
    outputPre = Text(Trova, wrap=WORD, yscrollcommand=scrollbar.set)
    outputPre.pack()
    scrollbar.config(command=outputPre.yview)

    # Esecuzione finestra
    Finestra.mainloop()
