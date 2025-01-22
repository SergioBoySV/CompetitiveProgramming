s, t, n = map(int, input().split())
walkTime = [int(i) for i in input().split()]
rideTime = [int(i) for i in input().split()]
arrivalIntervals = [int(i) for i in input().split()]
totalTime = 0
flag = True


for i in range(n):
    totalTime += arrivalIntervals[i] + walkTime[i] + rideTime[i]

    if totalTime > t:
        flag = False
        break

if flag:
    print("yes")
else:
    print("no")

