flag = False

for i in range(5):
    line = input().lower()
    if "fbi" in line:
        print(i + 1, end=' ')
        flag = True

if flag is False:
    print("HE GOT AWAY!")