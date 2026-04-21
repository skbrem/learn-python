def line(length, content):
    if content == "":
        print(length * "*")
    else:
        print(length * content[0])

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")
