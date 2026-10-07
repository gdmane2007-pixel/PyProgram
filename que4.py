

correct_password = 1234
attempts = 0

for i in range(3):
    password = int(input("Enter password: "))
    attempts = attempts + 1

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong password")

if attempts == 3 and password != correct_password:
    print("Account Locked")