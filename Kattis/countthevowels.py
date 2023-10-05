string = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0

for char in string:
    if char in vowels:
        counter += 1

print(counter)