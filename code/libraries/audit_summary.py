import os
import datetime

alert_count = 0

with open("daily_report.txt", "r") as f:
    for line in f:
        if "Alert" in line:
            alert_count += 1

print(f"Audit complete: Found {alert_count} critical issues today")
