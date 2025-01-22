n, p, s = map(int, input().split())

for i in range(s):
    cards = [int(i) for i in input().split()]
    cards.pop(0)
    if p in cards:
        print("KEEP")
    else:
        print("REMOVE")