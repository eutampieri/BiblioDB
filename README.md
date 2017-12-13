# BiblioDB
*This software is written in Python and it manages book collections.*
You can use in two ways: 
* Single client mode, no API
* Server and clients mode, with API.

## Security
The API brought with this application ~is secure~ has serious flaws: don't use it. Use instead (../PHPBiblioDB)[this project] that supports the migration ~json files containing users and ip whitelist are encrypted.
This allows to have a server (that can be even a Raspberry Pi or an old PC) with all the informations and unlimited clients that request and send infos to the main server.~
### Server edition
The server can be headless: it only needs to be plugged to the power plug and to the LAN with an Ethernet cable. To avoid security problems, like getting the encryption key, it's recomended using an headless machine with any physical access to users. It's also preferrable that the server machine runs a linux server distribution because of its stability and its secure attitude. If you want to enable IP authentication in addition to user and pasword, every machine on the net that'll use BibilioDB needs a static IP, or the DHCP setted to not change IPs.

In line 46 of api.py you can turn on or off IP authentication by modifying variable value to True or False. This is useful if you want to use only a limited number of client to add or lend books.
```python
ipEnabled=True
```
Before running the first time the API you should modify defalut IPs and users on lines 45,61,62,63:
```python
ip={"127.0.0.1":"Server", "enter here IP":"enter description","...":"..."}#Not necessary if ipEnables=false
utenti={"enter username":"enter password", "enter username 1","enter password 1","...":"..."}
badge={"enter username":"enter userID","enter username 1","enter userID 1","...":"..."}
tipoUtenti={"enter username":"enter role","enter username 1","enter role 1","...":"..."}
#Administrator role must be "admin", but you can create other roles for other users that aren't admins
```
Then, after you performed the first run, kill the server, remove infos from dictionaries on lines 45,61,62,63 and restart the server.
##API
When used in Server Mode, BiblioDB provides a REST API and a JQuery Mobile WebApp, accessible via http://{serverip}:5000/static/index.html
###API URL Scheme
* */isbninfo/titolo/{isbn}* returns the title of a given ISBN
* */isbninfo/scheda/{title}* returns all the infos about a title
* */isbninfo/isbn/{title}* returns the ISBN of a given title
* */isbninfo/posizione/{isbn}* returns the position of a book
* */isbninfo/autore/{isbn}* returns a book's author given the isbn
* */lista* returns a human readable list of all books in the library
* */json* returns the database in json format
* */tsv* returns a TSV list of all books in the library
* */qrcode.png* returns a Qr Code containing the webapp's url. If the server isn't connected to the internet it gives the following:
```html
        {h1}Errore{/h1}{p}Connettere il server ad Internet.{br}{h2}Velocità Download:{/h2}{br}Modem 56 kbps:\t1s{br}ADSL:\t{1s{/p}
```
* */add/{user}/{password}/{title}/{isbn}/{author}/{position}* adds a book to the library. The password is sent in SHA512 format
* *presta/{user}/{password}/{isbn}/{LibraryUserID}/{Status}* lends a book. The password is sent in SHA512 format, LibraryUserID is the person who you lend the book and Status is the book state: 0 to lent and 1 to return books.

##Databases
There are three main databases, two of them encrypted using AES16.
All of them are Python dictionaries packed into a JSON file.
* The first, *bibliodb.json*, is the main database, with inside following dictionaries packed in this order: *ISBNuse, Book position, Title and ISBN, ISBN and Title, ISBN and Author, filename for TSV export, who owns the ISBN (Biblioteca means library), the maximum amount of days allowed for a lend, ISBN lending date*. This file is created the first time when starting the main program.
* The second, *bibliodb-utenti.json*, contains all users of the system with their IDs and their privileges. Unlike *bibliodb.json*, it's created the first time when running the API.
* The third, *ipWhitelist.json*, contains the IP whitelist, used for authentication. The file is created the first time while starting the API

##SetUp
### Windows:
* Download [this EXE](https://github.com/eutampieri/BiblioDB/releases)
* Run it and extract. 

### Mac OS X or Linux:
* Open a terminal and past the following code:
```
git clone https://github.com/eutampieri/BiblioDB.git
cd BiblioDB
python bibliodb_gui.pyw
```
