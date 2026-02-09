attempts = 0

while True:
    print("beginning of the while block")
    code = input("Please type in your PIN: ")
    attempts += 1

    print("attempts", attempts)
    print("condition1", attempts == 3)
    if attempts == 3:
        success = False
        break

    print("code", code)
    print("condition2", code == "1234")
    if code == "1234":
        success = True
        break

    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
