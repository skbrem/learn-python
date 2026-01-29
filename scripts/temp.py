temp = int(input("Please type in a temperature: "))
c = (temp - 32) / 1.8

if temp > 32:
    print(f"{temp} degrees Fahrenheit equals {c} degrees Celsius")

if temp < 32:
    print(f"{temp} degrees Fahrenheit equals {c} degrees Celsius")
    print("Brr! It's cold in here!")
