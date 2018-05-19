# def readFile():
name = input("Enter file :")
if len(name) <1 :
	name = 'mbox-short.txt'
handle = open(name)
#text =str(handle.read(name))
#newText = str(text)


#def makeList():
	#readFile()

words = list()


# fh = handle.split()
for line in handle:
	line = line.rstrip() #default split "blankspace"
	if not line.startswith('From '):continue
	line = line.split()
	# print()
	# print(line)
	# print()
	words.append(line[1]) #this line add the index[1] in list (which is email after [0] index) in the loop

	# 	print(words)

		print()
    
    
# def emailCount():
counts = dict()
for word in words:
	counts[word]=counts.get(word,0) +1
print(counts)
print()

# def maxCount():
bigcount = None
Bigword = None

for word, count in counts.items():
	if bigcount is None or count >bigcount:
		bigcount = count
		Bigword = word


print(Bigword,bigcount)

# def main():
	# readFile()
	# makeList()
	# emailCount()
	# maxCount()
	# print("Thank you for using this program.")

# if __name__ == '__main__':
	#main()

