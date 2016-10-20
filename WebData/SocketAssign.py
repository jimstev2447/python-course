''''
Program to make a simple web browser
Access a URL and download and view the data from the document
'''
# http://www.py4inf.com/code/romeo.txt
import socket

url = raw_input('Enter URL: ')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    domain = url.split('/')[2]
    mysock.connect((domain,80))
except:
    print 'Incorrect URL entered...'
    exit()

mysock.send ('GET '+ url +' HTTP/1.0\n\n')

while True:

    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data
