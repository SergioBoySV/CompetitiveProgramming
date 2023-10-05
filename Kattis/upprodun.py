import math
rooms = int(input())
teams = int(input())
counter = 0
teamsInRoom = math.ceil(teams / rooms)

for i in range(rooms):
    print("*" * teamsInRoom)
    counter += teamsInRoom
    if counter + teamsInRoom > teams:
        break

bruh = abs(teams - counter)
print("*" * bruh)
