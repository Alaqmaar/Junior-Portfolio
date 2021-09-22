def deleteChar(string, char):
	newString = string.replace(char, '')
	return newString

userInput = input('Enter any string: ')
delete = input('Input the chracter to delete from the string: ')

newStr = deleteChar(userInput, delete)

print('The string after deleting all occurances of', delete, 'is', newStr)