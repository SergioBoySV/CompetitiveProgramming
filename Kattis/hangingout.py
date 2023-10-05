limit, events = map(int, input().split())
total = 0
counter = 0

for i in range(events):
    line = input().split()  # enter/leave n
    people = int(line[1])  # turn the n from input into an int

    if line[0] == "enter":  # add people
        total += people
    elif line[0] == "leave":  # subtract people
        total -= people

    if total > limit:
        # if we exceed the limit, we note this in counter and
        # also decrease total by people because they were not allowed in!
        counter += 1
        total -= people

print(counter)
