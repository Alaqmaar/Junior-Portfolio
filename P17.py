# Program 6 - 17
# Program to print the pattern for a number input by the user

num = int(input('Enter a number to generate it\'s pattern: '))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
