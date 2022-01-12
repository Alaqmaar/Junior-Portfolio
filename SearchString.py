str = input('Enter the string: ')
ch = input("Enter the character to be searched: ")
count = 0

for character in str:
    if character == ch:
        count += 1

print('The character', ch, 'appeared in', str, count, 'times.')