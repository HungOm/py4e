import urllib.request
import json

url = input("Enter the link:- ")
file =urllib.request.urlopen(url).read()
data = json.loads(file.decode("utf-8"))
# print(data[count])


def main():
	# print(data)
	myList=list()
	# jsn=
	for i in data['comments']:
		num=i['count']
		myList.append(num)
	print(len(myList)," Characters")
	print("Sum: ",sum(myList))
	# 	total = myList.append(i)
	# print(sum(total))

if __name__ == '__main__':
	main()