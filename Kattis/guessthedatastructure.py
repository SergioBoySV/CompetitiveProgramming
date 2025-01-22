from collections import deque
stack = deque()
queue = deque()
pqueue = deque()  # ??
sBool, qBool, pqBool = True, True, True

for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 1:
        stack.append(y)
        queue.append(y)
        pqueue.append(y)
    elif x == 2:
        s = stack.pop(y)
        q = queue.pop(y)
        pq = pqueue.pop(y)

        if x != s:
            sBool = False
        if x != q:
            qBool = False
        if x != pq:
            pqBool = False

