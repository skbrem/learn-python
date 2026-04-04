import os
import datetime

with open("daily_report.txt", "r") as f:
    for line in f:
        if "Alert" in line:
            print(f"Critical item found: {line.strip()}")
