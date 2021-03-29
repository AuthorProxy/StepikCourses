# https://stepik.org/lesson/3366/step/7?unit=949
# Sample Input:
# -5
# 12
# Sample Output:
# 4.5

a = int(input())
b = int(input())

if a % 3 != 0:
    a += 3 - a % 3

b -= b%3
print((a+b)/2)
