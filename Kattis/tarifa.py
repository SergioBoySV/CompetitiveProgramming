megsPerMonth = int(input())
months = int(input())

total = 0
for x in range(months):
    total += int(input())

print(abs(total - months * megsPerMonth) + megsPerMonth)