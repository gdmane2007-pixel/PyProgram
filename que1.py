
total_days = int(input("Enter total working days: "))

present = 0
absent = 0

for i in range(total_days):
    status = input("Enter P for Present or A for Absent: ")

    if status == "P":
        present = present + 1
    elif status == "A":
        absent = absent + 1

attendance = (present / total_days) * 100

print("Present days:", present)
print("Absent days:", absent)
print("Attendance percentage:", attendance)

if attendance >= 75:
    print("Eligible for bonus")
else:
    print("Not eligible for bonus")