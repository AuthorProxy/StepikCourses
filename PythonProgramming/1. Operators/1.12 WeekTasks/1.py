# https://stepik.org/lesson/5047/step/1?unit=1086
# Sample Input:
# 3
# 4
# 5
# Sample Output:
# 6.0

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)
