import os
import datetime

with open("system.log", "w") as f: f.write("test")

filename = "system.log"

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d")

new_name = f"{timestamp}_{filename}"

os.rename(filename, new_name)

print(f"Backup now complete: {new_name}")
