from collections import deque
queue = deque()
counter = 0
n, t = map(int, input().split())
tasks = [int(i) for i in input().split()]
for i in tasks:
    queue.appendleft(i)


for i in range(len(queue)):
    a = queue.pop()
    b = queue.pop()
    c = a + b

    if c < t:
        queue.append(c)
        counter += 1
    else:
        break

print(counter + 1)

