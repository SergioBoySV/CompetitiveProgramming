counter = 0

for i in range(int(input())):
    line = input().lower()
    if "rose" in line:
        counter += 1
    elif "pink" in line:
        counter += 1

if counter == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(counter)
