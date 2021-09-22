# Program 6-11
# Find the factors of a number using while loop

num = int(input('Enter a number to find its factors: '))
print('Factors of a number using while loop')

i = 1

while i < num:
    if num % i == 0:
        print(i , end = ' ')
    i += 1

print()