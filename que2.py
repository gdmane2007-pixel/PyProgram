
# Q2. Second Highest Salary

salary = float(input("Enter salary 1: "))

highest = salary
second = 0

for i in range(4):
    salary = float(input("Enter next salary: "))

    if salary > highest:
        second = highest
        highest = salary
    elif salary > second and salary != highest:
        second = salary

print("Highest salary:", highest)
print("Second highest salary:", second)