num = int(input("Enter the number of employees: "))
employee = {}
totalSalary = 0

for i in range(num):
    name = input("Enter the name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    print()
    employee[name] = salary

print("\nEmployee Name\t\tSalary\n")

for name, salary in employee.items():
    print(name,"\t", salary)

for i in employee.values():
    totalSalary += i

print("Total salary:", totalSalary)
