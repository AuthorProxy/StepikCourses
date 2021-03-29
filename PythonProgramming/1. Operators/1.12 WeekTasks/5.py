# https://stepik.org/lesson/5047/step/5?unit=1086
# Sample Input 1:
# 8
# 2
# 14
# Sample Output 1:
# 14
# 2
# 8
# Sample Input 2:
# 23
# 23
# 21
# Sample Output 2:
# 23
# 21
# 23

max, min, other = a, b, c = int(input()), int(input()), int(input())

if b > max: max, min = b, a
if c > max: max, min, other = c, a, b
if (min > other): min, other = other, min

print(max, min, other, sep='\n')
