

highest = 0
lowest = 100

excellent = 0
good = 0
average = 0
poor = 0

for i in range(6):
    score = float(input("Enter employee score: "))

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    if score >= 90:
        print("Excellent")
        excellent = excellent + 1
    elif score >= 75:
        print("Good")
        good = good + 1
    elif score >= 50:
        print("Average")
        average = average + 1
    else:
        print("Poor")
        poor = poor + 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Excellent employees:", excellent)
print("Good employees:", good)
print("Average employees:", average)
print("Poor employees:", poor)