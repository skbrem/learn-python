import os
import datetime

events = ["User Login", "Database Backup", "Disk Full Alert"]
 
with open("daily_report.txt", "a") as f:
    for event in events:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        f.write(f"[{now}] {event}\n")

print(f"Report updated.")
