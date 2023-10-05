string = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
firstHalf = string[0:len(string) // 2]  # First half of string
secondHalf = string[len(string) // 2:]  # Second half of string
firstHalfTotal, secondHalfTotal = 0, 0
rotatedFirstHalf, rotatedSecondHalf, out = "", "", ""
# print(firstHalf)
# print(secondHalf)

# The next 2 for loops sum up the values of each character by their index in alphabet
for i in firstHalf:
    firstHalfTotal += alphabet.index(i)

for j in secondHalf:
    secondHalfTotal += alphabet.index(j)

# print(firstHalfTotal)
# print(secondHalfTotal)

# The next 2 for loops apply a rotation to all letters in the string
# based on the variables defined in the above for loops
for i in range(len(firstHalf)):
    char = firstHalf[i]
    rotatedFirstHalf += chr((ord(char) + firstHalfTotal - 65) % 26 + 65)
    # The 65's are there to make sure we stay within ASCII codes 65-90 (A-Z)

for i in range(len(secondHalf)):
    char = secondHalf[i]
    rotatedSecondHalf += chr((ord(char) + secondHalfTotal - 65) % 26 + 65)

# print(rotatedFirstHalf)

# Finally, this loop takes a char in rotatedFirstHalf and rotates it by the value of the
# char in ans2 based on its index in alphabet!
for i in range(len(rotatedFirstHalf)):
    char = rotatedFirstHalf[i]
    shift = alphabet.index(rotatedSecondHalf[i])
    out += chr((ord(char) + shift - 65) % 26 + 65)

print(out)

# firstHalf = [string[i] for i in range(0, int(len(string) / 2))]
# secondHalf = [string[i] for i in range(int(len(string) / 2), len(string))]
