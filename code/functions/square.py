def line(length, content):
    if content == "":
        print(length * "*")
    else:
        print(length * content[0])

def square(number, symbol):
    for i in range(number):
        line(number, symbol)

square(3, "0")

