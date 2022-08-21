import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter - ')
html = urllib.request.urlopen('https://www.yellow-pages.ph/locations/city-of-manila-metro-manila/page-1').read()
soup = BeautifulSoup(html, 'html.parser')


#lz = list()
# Retrive all of the anchor tags
tags = soup('a')
print(type(tags))
for tag in tags :
    print(tag.get('href', None))
