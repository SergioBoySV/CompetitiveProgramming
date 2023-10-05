distinct = []

for i in range(10):
    n = int(input()) % 42
    if n not in distinct:
        distinct.append(n)

print(len(distinct))
