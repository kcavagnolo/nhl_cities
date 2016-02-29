import numpy as np
import json
import urllib2
import os

api_key = os.environ.get('GOOGLE_API_KEY')
cities = [line.rstrip('\n') for line in open('nhl_cities.dat')]
outfile = open('nhl_geocoded.dat', 'w')
for c in cities:
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}"
    result = json.loads(urllib2.urlopen(url.format(urllib2.quote(c),
                                                   urllib2.quote(api_key))).read())
    status = result['status']
    if status == 'OK':
        coords = result['results'][0]['geometry']['location']
        s = ','.join((str(coords['lat']), str(coords['lng'])))
        outfile.write(str(s)+"\n")
    else:
        print('Last request was completed with a status:', status)
outfile.close()
