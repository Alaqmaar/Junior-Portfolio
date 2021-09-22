# Program 6-12
# Program to demonstrate the use of break statement in loop

num = 0
for num in range(10):
    num += 1
    if num == 8:
        break
    print('Num has value', num)