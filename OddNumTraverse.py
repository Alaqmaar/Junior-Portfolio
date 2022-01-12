# Program 6-8-2
# Print odd numbers in a given sequence

total = 0
count = 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if (num % 2) != 0:
        print(num, 'is an odd Number')