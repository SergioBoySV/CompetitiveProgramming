import math

n = int(input())

if n < 99:
    print(99)
elif n % 100 >= 49:
    print(int(math.ceil(n / 100)) * 100 - 1)

elif n % 100 <= 48:
    print(int(math.floor(n / 100)) * 100 - 1)