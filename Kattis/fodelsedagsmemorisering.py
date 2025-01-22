n = int(input())
friends = {}
nameList, rankList, dateList, out = [], [], [], []
counter = 0

for i in range(n):
    name, rank, date = input().split()
    friends[f"name{i}"] = name
    friends[f"rank{i}"] = rank
    friends[f"date{i}"] = date


