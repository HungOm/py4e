print()
print("String and List: Best Friends ")
print()

abc = "With three words "
stuff = abc.split()
print(stuff)

print(len(stuff))
print(stuff[0])

print()


for w in stuff:
	print(w)

# =======================================
print()
print("Splitgin : DelimiterS ")
print()

line = "first;second;third"
thing = line.split()
print(thing)
#>>['first;second;third']
print(len(thing))
# >>1

print()
print('Now, try another')
print()


thing = line.split(';')
print(thing)
# >>['first','second','third']
print(len(thing))
# >>3

# ============================================
print()
print("======"*3)
print()
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From '): continue
	words = line.split()
	print(words[2])

# Sat
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
# Fri
print()
print("======"*3)
print("Double Split Pattern")
print()

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From '): continue
	words = line.split()
	email = words[1] #stephen.marquard@uct.ac.za
	# print(email) #to degub
	pieces = email.split('@')
	print(pieces[1])

	#>> uct.ac.za
	#>> media.berkeley.edu
	#>> umich.edu
	#>> iupui.edu

