def line(length, content):
    if content == "":
        print(length * "*")
    else:
        print(length * content[0])

def shape(num1, symb1, num2, symb2):
    for i in range(num1):
        line(i + 1, symb1)
    for o in range(num2):
        line(num2, symb2)

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
