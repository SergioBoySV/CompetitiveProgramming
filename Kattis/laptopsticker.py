a, b, c, d = map(int, input().split())

print("1" if abs(a - c) > 1 and abs(b - d) > 1 else "0")
