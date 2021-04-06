password = input("Enter your password: ")
while len(password) < 6:
    print("Invalid password")
    password = input("Enter your password: ")
if len(password) >= 6:
    for n in range(len(password)):
        print("*", end="")
