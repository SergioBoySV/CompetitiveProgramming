n = int(input())
i = 0
dimensions = 3
counter = 0

while i < n:
    i += dimensions ** 2
    dimensions += 2
    counter += 1

print(counter)
