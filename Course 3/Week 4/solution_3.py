import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



# myList = list()


def main():
	url = input('Enter - ')
	count =int(input('Enter Count- '))
	position = int(input('Enter postion-'))
	for link in range(count):
		html = urllib.request.urlopen(url, context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')
		# Retrieve all of the anchor tags
		countDown = 0
		tags = soup('a')
		for tag in tags:
			countDown += 1
			if countDown == position:
				url = tag.get('href')
				print(url)
				if link == count-1:
					print(tag.contents[0])
					break


if __name__ == '__main__':
	main()


