num = int(input("Please type in a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative or zero.")
