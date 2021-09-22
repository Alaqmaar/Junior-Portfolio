def hyphenString(string):
    newString = ''
    for a in string:
        if a == ' ':
            newString += '-'
        else:
            newString += a
    return newString


userInput = input('Enter a string: ')

result = hyphenString(userInput)

print('The new string is:', result)