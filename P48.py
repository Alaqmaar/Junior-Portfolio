def deleteChar(string, char):
    newString = ''

    for a in string:
        if a == char:
            newString += ''
        else:
            newString += a

    return newString


userInput = input('Enter any string: ')
delete = input('Input the character to delete from the string: ')

newStr = deleteChar(userInput, delete)

print('The new string after deleting all occurances of', delete, 'is', newStr)