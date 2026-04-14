import subprocess
import sys

target = sys.argv[1]
total_memory = 0.0

raw_output = subprocess.check_output(["ps", "aux"], text=True)
lines = raw_output.split("\n")

for line in lines:
    if target and sys.argv[0] not in line:
        parts = line.split()
        
    
