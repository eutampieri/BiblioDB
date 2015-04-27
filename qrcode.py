# coding=utf8
import socket
import urllib
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("208.67.220.220",80))
url="http://qrfree.kaywa.com/?s=20&d=http://"+s.getsockname()[0]+":5000/static/index.html"
s.close()
try:
	urllib.urlretrieve(url,"QrCode.png")
#print url
except:
	print "Connettere il computer ad Internet.\n Velocità Download:\nModem 56 kbps:\t1s\nADSL:\t<1s"
else:
	print"File salvato in QrCode.png"