nStudents = int(input("Enter the number of students: "))

studentMarks = list()

for i in range(0, nStudents):
	mark = int(input("Enter the marks out of 100: "))
	studentMarks.append(mark)

tMarks = 0

for i in studentMarks:
	tMarks += i

avgMarks = tMarks/len(studentMarks)

print("Total Marks:", tMarks)
print("Average Marks: ", avgMarks)
