string = input()
counter = 0

for i in range(0, len(string), 3):
    if string[i] != "P":
        counter += 1

for i in range(1, len(string), 3):
    if string[i] != "E":
        counter += 1

for i in range(2, len(string), 3):
    if string[i] != "R":
        counter += 1

print(counter)