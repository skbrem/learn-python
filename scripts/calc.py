num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
op = input("Operation: ")

if op == "add":
    sum1 = num1 + num2
    print(f"{num1} + {num2} = {sum1}")

if op == "multiply":
    sum2 = num1 * num2
    print(f"{num1} * {num2} = {sum2}")

if op == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
