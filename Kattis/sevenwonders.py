import math
string = input()
length = len(string)

T = [i for i in string if i == "T"]
C = [i for i in string if i == "C"]
G = [i for i in string if i == "G"]

total = (len(T) ** 2) + (len(C) ** 2) + (len(G) ** 2)

print(total)