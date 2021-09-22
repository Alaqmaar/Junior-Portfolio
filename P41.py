st = input('Input a string: ')
newstr = ''

for character in st:
    if character in 'aeiouAEIOU':
        newstr += '*'
    else:
        newstr += character

print(newstr)