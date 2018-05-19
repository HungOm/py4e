print("Counting Pattern")
print("======"*3)
print()

counts = dict()
line = input ("Enter a line of text : ")
words = line.split(' ')

print('Words: ', words)

print('counting .....')
for word in words:
	counts[word] = counts.get(word,0) + 1
print('Counts:', counts)
# ---------------
print()
print("Definit Loops and Dictionaries")

print()
for key in counts:
	print(key,counts[key])