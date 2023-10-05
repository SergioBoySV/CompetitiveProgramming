total = 0

for i in range(int(input())):
    nums = [float(i) for i in input().split()]
    total += nums[0] * nums[1]

print(total)
