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

# finalList = list()


for tag in tags:
	newtag =tag.get('href')
	myList.append(newtag)
# print(myList)
numBer =myList[2]
# print(numBer)


def main():
	countDown = 0
	name = []
	while countDown <= count:
		# link = []
		empty_lst = name
		if empty_lst not None:
			print(name[position])
			continue
		elif empty_lst ==[]:
			newurl = numBer
			html= urllib.request.urlopen(newurl, context=ctx).read()
			soup = BeautifulSoup(html, 'html.parser')
			links = soup('a')
			newList = list()

			for myTag in links:
				link =myTag.get('href',None)
				name.append(link)
			# linkList= newList[position]
				# linkList = newList[position]
				# name.append(newList)
			print("First", len(name))
			# print('First',len(name))
			# empty_lst[]=empty_lst[0]
			# break
		else:
			url2 = empty_lst[position]
			html = urllib.request.urlopen(url2, context=ctx).read()
			links = soup('a')
			# myList=[]
			# finalList =list()
			for myPthertag in links:
				newItem =myPthertag.get('href', None)
				name.append(newItem)
			print('-------------------')

				# MynewList =finalList[position] 
				# print(finalList)
			# empty_lst.append(MynewList)
				# _link = myList[position]
			# empty_lst.append(_link[position])
			# print(finalList)
		# finalPrint=empty_lst[position]
		# print(finalPrint)
		# print('Second',empty_lst)
		countDown = countDown + 1
		

if __name__ == '__main__':
	main()