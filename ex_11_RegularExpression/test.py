import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

site = input('Enter --->')
html = urllib.request.urlopen(site).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags :
	print(tag.get('href', None))
