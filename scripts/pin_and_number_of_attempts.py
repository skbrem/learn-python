# this is my attempt at this. It was correct but I see how the model solution is more elegant. 

attempts = 0

while True:
    pin = input("PIN: ")
    attempts += 1

    if attempts == 1 and pin == "4321":
        print("Correct! It only took you one single attempt!")
        break

    if pin != "4321":
        print("Wrong")

    if pin == "4321":
        print(f"Correct! It took you {attempts} attempts")
        break

