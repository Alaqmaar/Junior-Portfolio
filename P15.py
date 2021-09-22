# Program 6 - 15
# Program to demonstrate the use of continue statement
# Prints values from 0 to 6 except 3

for num in range(6):
    num += 1

    if num == 3:
        continue

    print('Num has value', num)

print('End of loop')
