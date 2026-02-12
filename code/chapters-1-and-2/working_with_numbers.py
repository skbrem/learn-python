total = 0
count = 0
positive = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish. ")

while True:
    num = int(input(""))
    if num == 0:
        break
    total += num
    count += 1

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(f"...the program asks for numbers...")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {(total / count)}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

