# https://stepik.org/lesson/3367/step/7?unit=950
# Sample Input 1:
# aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# abc
# Sample Output 2:
# a1b1c1

s = input()
temp = s[0]
count = 0

for i in s:
    if i == temp:
        count += 1
    else:
        print(temp, count, sep='', end='')
        temp = i
        count = 1

print(temp, count, sep='', end='')
