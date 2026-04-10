import subprocess

try:
    raw_output = subprocess.check_output(["ip", "addr"], text=True)

    print("--- SCANNING NETWORK INTERFACES ---")

    lines = raw_output.split("\n")

    for line in lines:
        if "inet" in line and "127.0.0.1" not in line:
            clean_line = line.strip()
            print(f"Active IP address found: {clean_line}")

except Exception as e:
    print(f"Could not run the network scan. Error: {e}")
