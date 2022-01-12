dict1 = {'Mohan':95, 'Ram':89, 'Suhel':92, 'Sangeeta':85}

# Indexing a dictionary
print('\nIndexing a dictionary')
print(dict1['Mohan'])

# Adding an element to a dictionary
dict1['Meena'] = 94
print('\nAdding an element to a dictionary')
print(dict1)

# Modifying an element in a dictionary
dict1['Mohan'] = 80
print('\nModifying an element in a dictionary')
print(dict1)

# Check if a key is present in a dictionary
print('\nCheck if a key is present in a dictionary')
print('Mohan' in dict1, '\n' + str('Rohan' in dict1))

# Traversing a dictionary
print('\nTraversing a dictionary')
for key in dict1:
    print(str(key) + ":" + str(dict1[key]))

# Alternative traversing a dictionary
print("\nAlternative traversing a dictionary")
for key, value in dict1.items():
    print(str(key) + ":"  + str(value))

# Length of a dictionary
print('\nLength of a dictionary')
print(len(dict1), 'elements')

# List of keys of a dictionary
print('\nList of keys of a dictionary')
print(dict1.keys())

# List of values of a dictionary
print('\nList of values of a dictionary')
print(dict1.values())

# Get a list of tuples with keys and values
print("\nGet a list of tuples with keys and values")
print(dict1.items())

# Get value for a coresponding key
print("\nGet value for a coresponding key")
print(dict1.get("Mohan"))

# Delete an items with given key
print('\nDelete an items with given key')
del dict1['Ram']
print(dict1)

# Clear all elements of a dictionary
print("\nClear all elements of a dictionary")
dict1.clear()
print(dict1)
