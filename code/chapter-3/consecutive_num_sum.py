limit = int(input("Limit: "))
total = 0
current = 1

while total < limit:
    total += current
    current += 1

print(total)
