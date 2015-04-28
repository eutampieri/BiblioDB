#!/bin/bash
echo Benvenuti nel processo di configurazione di BiblioDB!
echo Per prima cosa modificare la password del proprio account.
echo Se si sta eseguendo BiblioDB Linux, la password attuale dovrebbe essere bibliodb
passwd
mv bibliodb.json bibliodb.json.old
mv bibliodb-utenti.json bibliodb-utenti.json.old
mv ipWhitelist.json ipWhitelist.json.old
mv jsonvalidator.out jsonvalidator.out.old
read nutenti
for i in $(seq 0 "$nutenti" 1)
  do
     echo "Welcome $i times"
 done 