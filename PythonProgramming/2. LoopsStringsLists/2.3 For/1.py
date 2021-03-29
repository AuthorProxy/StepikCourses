# https://stepik.org/lesson/3366/step/3?unit=949
# Sample Input 1:
# 7
# 10
# 5
# 6
# Sample Output 1:

#    5  6
# 7  35 42
# 8  40 48
# 9  45 54
# 10 50 60
# Sample Input 2:
# 5
# 5
# 6
# 6
# Sample Output 2:
#   6
# 5 30
# Sample Input 3:
# 1
# 3
# 2
# 4
# Sample Output 3:
#   2 3 4
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('', end='\t')
for j in range(c,d+1):
    print(j, end='\t')

print()
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c,d+1):
        print(i*j, end='\t')
    print()
