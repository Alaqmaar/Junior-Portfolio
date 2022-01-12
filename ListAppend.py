nList = int(input("Enter the number of elements: "))

list1 = []
for i in range(0, nList):
	iList = int(input("Enter the element of the list: "))
	list1.append(iList)

print("Your list is:", list1)

rList = int(input("Enter the index of the element to remove: "))
pList = list1.pop(rList)

fList = []
for i in list1:
	if i != pList:
		fList.append(i)

print("Modified List:", fList)

fList = []
pList = list1[rList]

for i in list1:
	if i != pList:
		fList.append(i)

print("Modified List:", fList)
