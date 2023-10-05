for i in range(int(input())):
    x, y, z = map(int, input().split())
    if y - z > x:
        print("advertise")
    elif y - z < x:
        print("do not advertise")
    else:
        print("does not matter")