import os
import json

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except:
    print(f"Error loading config file: {e}")
    config = {"log_dictionary": ".", "search_term": "ERROR"}

folder = config["log_dictionary"]
term = config["search_term"]

print(f"Starting Audit on folder: {folder}")
print(f"Searching for: {term}")
