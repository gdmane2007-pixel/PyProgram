


suspicious_count = 0
suspicious_total = 0

for i in range(8):
    amount = float(input("Enter transaction amount: "))

    if amount > 100000:
        print("Suspicious Transaction")
        suspicious_count = suspicious_count + 1
        suspicious_total = suspicious_total + amount
    else:
        print("Normal Transaction")

print("Suspicious transactions:", suspicious_count)
print("Total suspicious value:", suspicious_total)