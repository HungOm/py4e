import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


tags =soup('span')
# lst[0] = list()
newList = []

def main():
	for tag in tags:

		newList= tag.contents[0]
		# lst[tag] = tag.strip()
		# int(tag.contents[0])
		# print(numbers)
		# lt = numbers.split()
		# lst.append(lt[0])
		# print(lst[0])

		# newList.append(lst)
		# print(newList)
		# for y in lst:
			# newList.append(y)
			# print(newList)
			# print(y)

		

if __name__ == '__main__':
	main()
