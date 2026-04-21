def line(length, content):
    if content == "":
        print(length * "*")
    else:
        print(length * content[0])

line(7, "%")
line(10, "LOL")
line(3, "")
