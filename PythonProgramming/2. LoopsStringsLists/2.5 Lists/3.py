# https://stepik.org/lesson/3368/step/11?unit=951
# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3
# Sample Input 4:
# 1 1 1 1 1 2 2 2
# Sample Output 4:
# 1 2

list = [int(i) for i in input().split()]

ind = 0
list_len = len(list)
list.sort()

while ind < list_len:
    total_count = list.count(list[ind])
    if total_count > 1:
        print(list[ind], end=' ')
    ind += total_count
