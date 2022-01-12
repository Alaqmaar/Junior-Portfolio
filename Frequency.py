n = int(input('Enter a number: '))
count = 0
m = n
print('Digit Frequency Percent')
for i in range(0, 10, 1):
    count = 0
    n = m
    Len = 0
    while n > 0:
        digit = n % 10
        if i == digit:
            count += 1
        n = n // 10
        Len += 1
    if count > 0:
        print(i, '\t\t', count, '\t\t', round((count / Len * 100), 1))
