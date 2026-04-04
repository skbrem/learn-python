ports = [21, 22, 80, 443, 8080]

for port in ports:
    print(f"Scanning {port}")
    if port == 443:
        print(f"[SUCCESS] HTTPS Port found! Stopping scan")
        break

print(f"Scanning complete")
