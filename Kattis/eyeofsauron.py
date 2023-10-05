string = input()
string = string.split("()")

if len(string[0]) == len(string[1]):
    print("correct")
else:
    print("fix")