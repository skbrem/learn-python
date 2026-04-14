import os
import json
import sys

key = os.getenv("MONITOR_API_KEY")

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <config_file>")
    exit(1)

config_file = sys.argv[1]

if not key:
    print(f"The environmental variable has not been set.")
    exit(1)
try:
    with open(config_file, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: The file '{config_file}' does not exist")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: '{config_file}' is not a valid JSON file.")
    exit(1)

print(f"API key successfully loaded: {key}")
print(f"Loaded {len(data['targets'])} targets from config.")
