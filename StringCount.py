# Write a program to count the number of times a value appears in a string

string = input("Enter a string: ")
countValue = input("Enter character to be searched: ")
count = 0

for i in string:
    if i == countValue:
        count += 1

print(countValue, "appeared in", countValue + ", ", count, "times.")
