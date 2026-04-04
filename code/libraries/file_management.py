import os
if not os.path.exists("Scripts"):
    os.mkdir("Scripts")

files = os.listdir(".")

for filename in files:
    if filename.endswith(".py"):
        print(f"Moving {filename}...")
        os.rename(filename, f"Scripts/{filename}")
