word = input("Word: ")

length = len(word)

new_length = 28 - length

left_space = new_length // 2
right_space = new_length - left_space

print(30*"*")
print (f"*{right_space * ' '}{word}{left_space * ' '}*")
print( 30*"*")
