string = [int(i) for i in input() if i != "-"]
nums = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
total = 0

for i in range(len(string)):
    total += string[i] * nums[i]

if total % 11 == 0:
    print(1)
else:
    print(0)