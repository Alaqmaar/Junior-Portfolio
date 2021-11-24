nStudents = int(input("Enter the number of students: "))

list1 = list()

for i in range(nStudents):
	student = input("Enter the name of your student: ")
	list1.append(student)

sStudent = input("Enter the name of the student to be searched: ")

found = False

for i in list1:
	if i == sStudent:
		print(i," was found in the database")
		found = True

if not found:
	print("No results.")
		
