import os

files = os.listdir(".")

for filename in files:
    size = os.path.getsize(filename)
    if size > 100:
        print(f"ALERT: {filename} is too large: {size} bytes")
    else:
        print(f"SAFE: {filename} is {size} bytes")
