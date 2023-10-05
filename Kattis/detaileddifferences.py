for testCases in range(int(input())):
    line1 = input()
    line2 = input()
    print(line1)
    print(line2)

    for i in range(len(line1)):
        if line1[i] != line2[i]:
            print("*", end='')
        else:
            print(".", end='')

    print("\n")
