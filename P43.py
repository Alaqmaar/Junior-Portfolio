Str = input('Enter a string: ')
str1 = ''
str2 = ''
str3 = ''

vowels = 'AEIOUaeiou'
for ch in Str:
	if ch in vowels:
		str1 += ch
	else:
		if ch.isalpha():
			str2 += ch
		else:
			if ch.isalnum():
				str3 += ch

print('The vowels in', Str, 'are =', str1)
print('The consonants in', Str, 'are =', str2)
print(str3)
