import os

files = os.listdir(".")

# This version was written by me but there's a better way of doing it.
# Here, this would also flat a file called "my.python.notes.txt"
# To get around this, use `endswith()`
#for filename in files:
#    if ".py" in filename:
#        print(f"Found script: {filename}")
#    else:
#        print(f"Other file: {filename}")

for filename in files:
    if filename.endswith(".py"):
        print(f"Found script: {filename}")
    else:
        print(f"Other file: {filename}")

