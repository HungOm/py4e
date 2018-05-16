stuff = "Hello\nWorld!"
print(stuff)


print("This is a file processing execise")
print("Date : 16/05/2018")

File_input = input("Enter the file name: ")


fhand = open(File_input,encoding ="utf-8")


print("Note: Without char# encoding>> it will show\nThe following error.")

#Traceback (most recent call last):
  #File "C:\Users\User\Desktop\P4e\Course 2\Week 3\File.py", line 12, in <module>
    #inp = fhand.read()
  #File "C:\Users\User\AppData\Local\Programs\Python\Python36-32\lib\encodings\cp1252.py", line 23, in decode
    #return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1748: character maps to <undefined>

inp = fhand.read()

print(len(inp)) #print the total number of words in the file.
# print(len(inp[:20])


# -------------------------------------------------------------

print("Seaching Through a File(fixed")


fhand = open("mbox-short.txt")
for line in fhand:
	line = line.rstrip()
	if line.startswith('From: ') :
		print(line)

# >> From: stephen.marquard@uct.ac.za
# >> From: louis@media.berkeley.edu
# >> From: zqian@umich.edu
# >> From: rjlowe@iupui.edu
# >> From: zqian@umich.edu
# >> From: rjlowe@iupui.edu
# .
# .
# # .
# 		continue
# 	print(line)


# --------------------------------------------

print()

print("another exercise using \"in\" ")

print()


fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line :
		continue
	print(line)

# ==============================

print()
print('handling errors')
print()

fname = input("Enter the file name: ")

try:
	fhand = open(fname)

except:
	print('File cannot be opened: ',fname)
	quit()

count = 0

for line in fhand:
	if line.startswith('Subject: ') :
		count = count +1
print('There were', count, 'subject line in',fname)