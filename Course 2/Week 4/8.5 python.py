fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
   
    #print("debug2:",words)
    if len(words)==0:continue
    if words[0]!="From":continue

    
    print(words[1])
    count+=1
#ount=len(words)
print("There were", count, "lines in the file with From as the first word")
