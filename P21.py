# String transversal using for loop
str1 = 'Hello World!'
for ch in str1:
    print(ch, end = '')

print('\n\n')

# String transversal using while loop
str1 = 'Hello World!'
index = 0
while index < len(str1):
    print(str1[index], end = '')
    index += 1

print('\n\n')

# Reversing string using for loop
str1 = 'Hello World!'
for i in range(len(str1)-1,-1,-1):
    print(str1[i], end = '')

print('\n\n')

# Reversing string using while loop
str1 = 'Hello World!'
index = len(str1)-1
while index > -1:
    print(str1[index], end = '')
    index -= 1

print('\n\n')

# Reverse string using for loop without index
str1 = 'Hello World!'
rev = ''
for ch in str1:
    rev = ch + rev
print(rev)
