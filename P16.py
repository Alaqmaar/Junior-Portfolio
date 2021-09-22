# Program 6 - 16
# Demonstrate working of nested for loop

for var1 in range(3): # First Loop Range = 0 to 3
    print('Iteration', var1, 'of outer loop') # Prints statement and value of var1

    for var2 in range(2): # Second Loop Range = 0 to 2
        print(var2 + 1) # Prints var2 + 1

    print('Out of inner loop') # Doesn't matter

print('Out of outer loop') # Doesn't matter
