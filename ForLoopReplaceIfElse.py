# Program 6 - 19
# The following program uses a for loop nested inside an if..else
# block to calculate the factorial of a given number

num = int(input('Enter a number: '))
fact = 1

if num < 0:
    print('Sorry, the factorial of negative numbers is not possible.')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        fact *= i
    print('factorial of', num, 'is', fact)
