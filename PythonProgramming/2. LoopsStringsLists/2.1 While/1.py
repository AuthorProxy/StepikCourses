# https://stepik.org/lesson/3364/step/11?unit=947
# Sample Input 1:
# 5
# -3
# 8
# 4
# 0
# Sample Output 1:
# 14
# Sample Input 2:
# 0
# Sample Output 2:
# 0

i = int(input())
s = 0
while i != 0:
    s += i
    i = int(input())

print(s)
