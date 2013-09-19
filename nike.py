import urllib2
import json

nike_data_uri = 'http://manufacturingmap.nikeinc.com/maps/export_json?'
nike_json = urllib2.urlopen(nike_data_uri).read()
nike_data = json.loads(nike_json)

# number of workers per city
z = {}
for x in data:
    location = x['city'].lower().strip() + ', ' + x['country'].lower().strip()
    if loc in z:
        z[location] += x['workers']
    else:
        z[location] = x['workers']