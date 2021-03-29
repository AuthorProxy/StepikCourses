# https://stepik.org/lesson/3368/step/10?unit=951
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10

list = [int(i) for i in input().split()]

ind = 0
list_len = len(list)

for i in list:
    if list_len == 1:
        print(i, end='')
        continue

    prev_pos = ind - 1
    next_pos = ind + 1

    if next_pos >= list_len:
        next_pos = 0

    print(list[prev_pos] + list[next_pos], end=' ')
    ind += 1
