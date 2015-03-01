import pickle
import json
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
ISBNborrowDate = {}
nomeFile = "db_libri"
borrowTime = 30
nomeFile="BookDB"
try:
    o=open('bibliodb.pickle','r')
except IOError:
    o=open('bibliodb.pickle','w')
    pickle.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown,borrowTime),o)
    o.close()
else:
    o.close
finally:
    with open('bibliodb.pickle','r') as o:
                    ISBNuse, isbnPos, titleIsbn, isbnTitle,isbnAuthor,nomeFile=pickle.load(o)
                    o.close
j=open('bibliodb.json','w')
json.dump((ISBNuse,isbnPos,titleIsbn,isbnTitle,isbnAuthor,nomeFile,ISBNown,borrowTime),j)
j.close()
print "OK"
