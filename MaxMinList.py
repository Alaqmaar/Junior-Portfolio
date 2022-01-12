nElements = int(input("Enter number of elements in the list: "))
print("Enter", nElements, "of the list: ")
list1 = []

for i in range(0, nElements):
	element = int(input("Enter the element: "))
	list1.append(element)

print()

print("Your list is:", list1)

print("Max: ", max(list1))
print("Min: ", min(list1))

eMax = list1[0]
for i in list1:
	if i > eMax:
		eMax = i

print("Max (without built-in function): ", eMax)

eMin = list1[0]
for i in list1:
	if i < eMin:
		eMin = i

print("Min (without built-in function):", eMin)
