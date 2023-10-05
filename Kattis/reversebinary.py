import math
num = int(input())
binDigits = []
total = 0
exponent = 0

while num > 0:
    r = num % 2
    num = math.floor(num / 2)
    binDigits.insert(0, r)

for i in binDigits:
    total += i * 2 ** exponent
    exponent += 1

print(total)
