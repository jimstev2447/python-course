import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = 'UCSD'

url = serviceurl + urllib.urlencode({'sensor':'false','address':address})

print 'Retrieving URL: ', url

info = urllib.urlopen(url).read()

print 'Retrieved', len(info), 'characters'

data = json.loads(info)

print 'place id', data['results'][0]['place_id']
