string = input("Please type in a  string: ")
index = 0

limit = len(string)

while index < limit:
        print(string[0:index+1])
        index += 1

# ==== Model Solution ==== #
# string = input("Please type in a string: ")
# 
# length = 1
# while length <= len(string):
#     print(string[0:length])
#     length += 1

