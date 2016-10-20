import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_322429.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

total = 0

for tag in tags:
    total = total + int(tag.contents[0])

print total
