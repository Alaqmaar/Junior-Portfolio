ODD = {1:"One", 3:"Three", 5:"Five", 7:"Seven", 9:"Nine"}

# Displaying the keys
print("Keys: ")
for i in ODD.keys():
    print(i)
print()

# Display the values
print("Values: ")
for i in ODD.values():
    print(i)
print()

# Display the items
print("Items: ")
for i, v in ODD.items():
    print(i, '\t', v)
print()

# Check if 7 is present
print("7 is in ODD dictionary: ",7 in ODD)
print()

# Check if 2 is present
print("2 is in ODD dictionary: ",2 in ODD)
print()

# Delete key 9 from the dictionary
del ODD[9]
print(ODD)
