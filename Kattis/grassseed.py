n = float(input())
total = 0

for testCases in range(int(input())):
    x, y = map(float, input().split())
    total += x * y * n

print('%.7f' % total)