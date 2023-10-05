def GCD(x, y):
    while y != 0:
        (r := x % y)
        (x := y)
        (y := r)

    return x

num1, num2 = input().split(" ", 1)
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    out = GCD(num1, num2)
else:
    out = GCD(num2, num1)

print(out)