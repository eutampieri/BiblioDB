# BiblioDB
*This software is written in Python and it manages book collections.*
You can use in two ways: 
* Single client mode, no API
* Server and clients mode, with API.

##Security
The API brought with this application is secure: json files containing users and ip whitelist are encrypted.
This allows to have a server (using a Raspberry Pi or a old PC) with all the informations and unlimited clients that request and send infos to the main server.
###Server edition
The server MUST NOT use a keyboard, a mouse or a monitor: it only needs to be plugged to the power plug and to the LAN with an Ethernet cable to avoid security problems. It's also preferrable that the server machine runs a linux server distribution because of its stability and its secure attitude. Evry machine on the net that'll use BibilioDB needs a static IP, or the DHCP setted to not change IPs.
##API
When used in Server Mode, BiblioDB provides a REST API and a JQuery Mobile WebApp, accessible via http://<serverip>:5000/static/index.html
It's also provided a qrcode generator!
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