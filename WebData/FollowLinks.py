import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter Count: '))
position = int(raw_input('Enter Position: '))

while count >= 0:
    print 'Retrieving: ', url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    tags = soup('a')
    taglist = []
    
    for tag in tags: taglist.append(tag.get('href',None))
    
    url = taglist[position -1]
    count = count - 1
