rooms = int(input())
z = 0
flag = True

for i in range(rooms):
    x, y = map(int, input().split())
    z += abs(x - y)
    if y < x + z:
        flag = False
        break

if flag:
    print("possible")
else:
    print("impossible")