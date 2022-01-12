# Gives substring starting from index 1 to 4
str1 = 'Hello World'
print(str1[1:5])

# Give substring starting from 7 to 9
print(str1[7:10])

# Index that is too big is truncated down to the end of string
print(str1[3:20])

# First index > second index results in an empty '' string
print([str1[7:2])