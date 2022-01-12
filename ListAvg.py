# Print the total and average given sequence of numbers using for loop
count = [10, 20, 30 , 40, 50]
total = 0
for num in count:
    total += num

avg = total / len(count)

print('Total =', total)
print('Average =', avg)