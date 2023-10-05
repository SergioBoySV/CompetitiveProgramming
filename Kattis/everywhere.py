distinctCities = []
for testCases in range(int(input())):
    trips = int(input())

    for x in range(trips):
        city = input()
        if city not in distinctCities:
            distinctCities.insert(0, city)
        else:
            continue

    print(len(distinctCities))
    distinctCities.clear()
