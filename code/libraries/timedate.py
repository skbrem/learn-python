import datetime

# Get the current time
now = datetime.datetime.now()

# Format it into a string we can use in a filename (Year-Month-Day)
timestamp = now.strftime("%Y-%m-%d")
print(f"Today's date is: {timestamp}")
