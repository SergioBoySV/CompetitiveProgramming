string = input().split()
flag = False

for i in string:
    count = string.count(i)
    if count >= 2:  # >= 2 because i is already in the string, so we gotta check for more than 1 (eg >=2)
        flag = True
        break

if flag is False:
    print("yes")
else:
    print("no")


