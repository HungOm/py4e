
fname=input("Enter file name: ")
fh=open(fname)
lst=list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    for c in line:
        if c not in lst:
            lst.append(c)

lst.sort()#crucial indenticaton for prper exit//..>>check below for example
print(lst)
     #remove comment to test the code below
        #lst.sort()
        #print(lst)
