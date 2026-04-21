def line(length, content):
    if content == "":
        print(length * "*")
    else:
        print(length * content[0])

def square_of_hashes(number):
    for i in range(number):
        line(number, "#")

square_of_hashes(5)
