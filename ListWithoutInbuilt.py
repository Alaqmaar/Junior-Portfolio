print("With Inbuilt Functions:\n")

list1 = list()

nList = int(input("Enter the length of your list: "))

for i in range(nList):
    element = int(input("Enter the element of your list: "))
    list1.append(element)

print(list1)

posElement = int(input("Enter the position of the element to be deleted: "))

# noinspection PyBroadException
try:
    list1.pop(posElement - 1)
except:
    print("No results found.")

print("Modified list:", list1)

valElement = int(input("Enter the value of the element to be deleted: "))

try:
    list1.remove(valElement)
except:
    print("No results found.")

print("Modified List:", list1)

print("Without Inbuilt Functions:\n")

list1 = list()
list2 = list()

nList = int(input("Enter the length of your list: "))

for i in range(nList):
    element = int(input("Enter the element of your list: "))
    list1.append(element)

print(list1)

posElement = int(input("Enter the position of the element to be deleted: "))

try:
    delElement = list1[posElement - 1]

    for i in list1:
        if i != delElement:
            list2.append(i)

except:
    print("No results found.")

print(list2)

list1 = list2
list2 = []
found = False

valElement = int(input("Enter the value of the element to be deleted: "))

try:
    for i in list1:
        if i != valElement:
            list2.append(i)
        else:
            found = True

    if not found:
        print("No results found.")

except:
    print("No results found.")

print(list2)
