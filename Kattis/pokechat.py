import re
key = input()

code = re.findall('.{1,3}', input())  # Using regex to split the string every 3 chars

code = [i.lstrip('0') for i in code]  # Removing all leading zeros from the string (001 -> 1)
code = [int(i) for i in code]  # Converting to int

for i in code:
    print(f"{key[i - 1]}", end='')
