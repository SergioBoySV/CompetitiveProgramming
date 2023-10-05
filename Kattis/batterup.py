n = int(input())
nums = [int(i) for i in input().split()]
total = 0

for x in nums:
    if x == -1:
        n -= 1
    else:
        total += x

print(total / n)
