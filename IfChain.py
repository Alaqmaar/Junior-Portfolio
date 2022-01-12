# ++++++++++++++++++
# + Above 90%  + A +
# + 80% to 90% + B +
# + 70% to 80% + C +
# + 60% to 70% + D +
# + Below 60%  + E +
# ++++++++++++++++++

marks = int(input("Enter the grade: "))

if marks > 100 or marks < 0:
    print('Error,', marks, 'is not a valid input')
elif marks < 60:
    print('E')
elif marks < 70:
    print('D')
elif marks < 80:
    print('C')
elif marks < 90:
    print('B')
else:
    print('A')
