out = 0
exp = 0
num = 0

for i in range(int(input())):
    numDigits = list(input())[::-1]
    powerOf = int(numDigits.pop(0))
    numDigits = [int(i) for i in numDigits]

    for j in numDigits:
        num += j * 10 ** exp
        exp += 1

    out += num ** powerOf
    exp = 0
    num = 0

print(out)