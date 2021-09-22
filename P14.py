# Program 6-14
# Write a python program to check if a number is prime or not

num = int(input('Enter a number to check if it\'s prime: '))
prime = True

if num > 1:
    for i in range(2, int(num/2)):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')
