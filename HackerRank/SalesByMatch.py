def sockMerchant(n, array):
    total = 0
    for i in range(n):
        pair = [j == i for j in array if j == i]
        return pair

        # if len(pair) % 2 == 0:
        #     total += len(pair)
        #
        # pair.clear()

    return total

arrayParam = [10, 20, 20, 10, 10, 30, 50, 10, 20]
for i in range(len(arrayParam)):









# print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
