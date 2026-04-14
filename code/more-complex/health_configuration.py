import json
import requests
import datetime

def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return "DOWN"

def log_result(url, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("server_health.log", "a") as log:
        log.write(f"[{timestamp}] - {url} - {status}\n")

try:
    with open("servers.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(F"Error: The configuration file could not be foundfound.")
except json.JSONDecodeError:
    print(F"Error: The configuration file is not a valid JSON.")

if "targets" in data:
    for url and in data:
        print(f"Checking the URL for each {url}")
        status = check_server(url)
        log_result(url, status)
        print(f"The {url} is {status}")
else:
    print(f"Error: The configuration file is missing the 'targets' list.")
