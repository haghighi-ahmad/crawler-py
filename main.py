import urllib
from bs4 import BeautifulSoup

params = urllib.urlencode({'spam': 1, 'eggs': 2})
f = urllib.urlopen("http://localhost/?%s" % params)

print f.read()
