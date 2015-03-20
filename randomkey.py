from random import randint
c=open("key.c",'w')
c.write('#include "stdio.h"\nvoid main(){\n\tprintf("'+str(randint(1111111111111111,9999999999999999))+'");\n}')