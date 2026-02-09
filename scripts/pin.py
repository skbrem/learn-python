attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # This is printed if the code was incorrect and there have been less than 3 attempts 
    print("Incorrect...try again!")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
