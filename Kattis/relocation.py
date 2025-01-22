x, testCases = map(int, input().split())  # x is redundant here, we never use it
locations = [int(i) for i in input().split()]

for i in range(testCases):
    a, b, c = map(int, input().split())

    if a == 1:
        locations[b - 1] = c
    elif a == 2:
        print(abs(locations[b - 1] - locations[c - 1]))
