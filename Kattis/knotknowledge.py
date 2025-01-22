n = int(input())
knotsToLearn = [int(i) for i in input().split()]
knotsLearned = [int(i) for i in input().split()]
out = [i for i in knotsToLearn if i not in knotsLearned]

print(out[0])

