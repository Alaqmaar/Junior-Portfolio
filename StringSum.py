def sumDigit(string):
    sum = 0
    for a in string:
        if (a.isdigit()):
            sum += int(a)
    return sum


userInput = input('Enter any string with digits: ')

result = sumDigit(userInput)

print('The sum if all digits in the string', userInput, 'is', result)