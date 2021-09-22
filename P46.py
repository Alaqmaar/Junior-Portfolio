def hyphenString(string):
    string.replace(' ', '-')


userInput = input('Enter a sentence: ')

result = hyphenString(userInput)

print('The new sentence is: ', result)