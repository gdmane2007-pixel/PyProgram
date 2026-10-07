
# Q3. Customer Transaction Risk Detector

low = 0
medium = 0
high = 0

for i in range(10):
    amount = float(input("Enter transaction amount: "))

    if amount < 10000:
        print("Low Risk")
        low = low + 1
    elif amount <= 50000:
        print("Medium Risk")
        medium = medium + 1
    else:
        print("High Risk")
        high = high + 1

print("Low Risk transactions:", low)
print("Medium Risk transactions:", medium)
print("High Risk transactions:", high)