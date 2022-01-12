userInput = input('Write a sentence: ')
totalChar = len(userInput)

print('Total Characters:', totalChar)

totalAlpha = totalDigit = totalSpecial = 0

for a in userInput:
    if a.isalpha():
        totalAlpha += 1
    elif a.isdigit():
        totalDigit += 1
    else:
        totalSpecial += 1

print('Total Alphabets:', totalAlpha)
print('Total Digits:', totalDigit)
print('Total Special:', totalSpecial)

totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1

print('Total Space:', totalSpace)


def convertToTitle(string):
    titleString = string.title()
    print('Input string in title case is', titleString)


if (userInput.istitle()):
    print('The string is already in title case.')
elif (totalSpace > 0):
    convertToTitle(userInput)
else:
    print('The string is of one word only.')