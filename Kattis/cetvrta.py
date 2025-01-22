xList = []
yList = []

for i in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

print(xList)
print(yList)

if xList[1] == xList[0]:
    xOut = xList[-1]
elif xList[]:
    xOut = xList[0]

if yList[1] == yList[0]:
    yOut = yList[-1]
else:
    yOut = yList[0]

print(f"{xOut}  {yOut}")




print(xList)
