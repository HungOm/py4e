import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)
url = input("Ener link here: ")
xml = urllib.request.urlopen(url)
data =xml.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
print("Count:", len(tree))
myList =[]

comments = tree.findall('comments/comment')
# print(len(comments))
for comment in comments:
    lst =comment.find('count').text
    myList.append(lst)
    # print(int(myList))
# print(myList)
myList = [int(i) for i in myList]
print("Sum : ", sum(myList))