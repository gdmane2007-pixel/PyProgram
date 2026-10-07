


total = 0
highest = 0
lowest = 0
high_months = 0

for i in range(12):
    sales = float(input("Enter monthly sales: "))

    total = total + sales

    if i == 0:
        highest = sales
        lowest = sales
    else:
        if sales > highest:
            highest = sales

        if sales < lowest:
            lowest = sales

    if sales > 100000:
        high_months = high_months + 1

average = total / 12
percentage = (high_months / 12) * 100

print("Total annual sales:", total)
print("Average monthly sales:", average)
print("Highest monthly sales:", highest)
print("Lowest monthly sales:", lowest)
print("High-sales months:", high_months)
print("Percentage of high-sales months:", percentage)