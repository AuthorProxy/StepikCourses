# https://stepik.org/lesson/3369/step/9?unit=952
# Sample Input 1:
# 5 8 2 7 8 8 2 4
# 8
# Sample Output 1:
# 1 4 5
# Sample Input 2:
# 5 8 2 7 8 8 2 4
# 10
# Sample Output 2:
# Отсутствует

lst = [int(i) for i in input().split()]
x = int(input())
was_found = False

for i in range(len(lst)):
    if lst[i] == x:
        was_found = True
        print(i, end=' ')

if not was_found:
    print('Отсутствует')
