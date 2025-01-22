percentages = [int(i) for i in input().split()]
letterGrades = ["A", "B", "C", "D", "E"]
grade = int(input())
flag = True

for i in range(len(percentages)):
    if grade >= percentages[i]:
        flag = False
        print(letterGrades[i])
        break

if flag:
    print("F")

