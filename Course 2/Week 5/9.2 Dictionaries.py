#One common use dictionaries is counting how often we "see" something


ccc = dict()
ccc["csev"] = 1
ccc ['cwen'] = 1
print(ccc)
{'csev':1,'cwen':1}
ccc['cwen'] = ccc ['cwen'] + 1

print(ccc)
print()
print('=========='*2)
print()
print("When there is a new name")
print()

print("This is a historgram")

counts = dict()
# names = ['csev','cwen','csev','zqian','cwen']
# for name in names:
#     try:
#         if name not in names:
#             counts[name] = 1
#         else:
#             counts[name] = counts[name]+1
#             continue
#     except:
#         KeyError
#         #continue
#         print("There is a KeyError in the program.\nPlease, Check your line and run again.\nThank you")
# print(counts)

names = ['csev','cwen','csev','zqian','cwen']
for name in names:
 	if name not in counts:
 		counts[name] = 1
 	else:
 		counts[name] = counts[name]+1 #Adding the value(which is the count number)
print(counts)
#>>{'csev': 2, 'cwen': 2, 'zqian': 1}


# ----------------------------
print()
print('=========='*2)
print()
print("Another way")
print()

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	counts[name]=counts.get(name,0)+1 #Adding the value(which is the count number)
print(counts)
#>>{'csev': 2, 'cwen': 2, 'zqian': 1}
