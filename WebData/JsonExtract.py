import urllib
import json

url ='http://python-data.dr-chuck.net/comments_322430.json'
fhand = urllib.urlopen(url)
info = json.loads(fhand.read())

total = 0 

for i in info['comments']:
    total = total + i['count']

print total

