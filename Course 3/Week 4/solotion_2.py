# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count =int(input('Enter Count- '))
position = int(input('Enter postion-'))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
myList = list()
# for tag in tags:
#     # print(tag.get('href', None))
#     num = tag.get('href',None)
#     myList.append(num)
# empty_lst = []

# for i in myList:
# 	empty_lst.append(i)
# newVal = empty_lst[2]
# print(newVal)

# for link in links:
# 	newLink = link.get('href')
# 	allLink.append(newLink)
# 	# lenght = len(allLink) - 1
timer = 0
empty_lst = []
while timer <= count:

	for tag in tags:
		num = tag.get('href', None)
		myList.append(num)
	newurl = myList[position]
	# print("THis is new url", newurl)
	print()
	# print()
	# print()
	url = newurl
	html = urllib.request.urlopen(url,context=ctx).read()
	soup = BeautifulSoup(html,'html.parser')

	links = soup('a')
	# allLink = list()

	for i in myList:
		empty_lst.append(i)
		# newVal = empty_lst[2]
	name =empty_lst[timer]
	timer = timer +1
	print('Retrieving:',name)
		# print(allLink)
