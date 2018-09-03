import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input ('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags

# tags = soup('a')
tags = soup('span')

def main():
	for tag in tags:
		# print(tag.get('href', None))
		print ('Contents:',tag.contents[0])

if __name__ == '__main__':
	main()