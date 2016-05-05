import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2})
f = urllib.urlopen("http://www.google.com/?%s" % params)
print f.read()
