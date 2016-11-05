import urllib
import xml.etree.ElementTree as ET

count = 0
url = 'http://python-data.dr-chuck.net/comments_322426.xml'

fhand = urllib.urlopen(url)

data = ET.fromstring(fhand.read())
lst = data.findall('comments/comment')

for item in lst:
    count = count + int(item.find('count').text)

print count
