x, y = map(int, input().split())
total = 0

for i in range(x):
    num = int(input())
    total += num

if total > y:
    print("Neibb")
else:
    print("Jebb")
    