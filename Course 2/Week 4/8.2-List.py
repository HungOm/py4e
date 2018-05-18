print()

print("Manipulating List")


# Slicing List

t = [9,41,12,3,74,15]

print(t[1:3])
#>> 42,12

#upto but not including


# -----------------------------

print()
print("Building a list from scratch")
print()

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
#>>['book', 99]

#list are mutable

# ---------------------


num = [3,41,12,9,74,15]

print(len(num))
#>> 6

print(max(num))
# >>74

print(min(num))
#>>3
print(sum(num))
#>>154
print(sum(num) / len(num))
#25.6
# ---------------------------


print("===============")
print()

total =0
count =0
while True:
	inp = input('Enter a number: ')
	if inp == 'done' :break
	value = float(inp)
	total = total + value
	count = count + 1
average = total / count
print('Average: ', average)


# -------------------------


print()
print("another loop, using \"List Data Structure\" to produce the same result")
print()

numlist = list()
while True :
	inp = input("Enter a number: ")
	if inp == "done": break
	value = float(inp)

	numlist.append(value)

average1 = sum(numlist)/len(numlist)
print("Average:", average1)


# ========================
print()
print("====================")
print()


