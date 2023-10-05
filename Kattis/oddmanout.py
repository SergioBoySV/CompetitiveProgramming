numTestCases = int(input())

for tesCases in range(numTestCases):
    numGuests = int(input())
    guests = [i for i in input().split()]

    for i in range(len(guests)):
        if not guests.count(guests[i]) >= 2:
            print(f"Case #{tesCases + 1}: {guests.pop(i)}")
            break