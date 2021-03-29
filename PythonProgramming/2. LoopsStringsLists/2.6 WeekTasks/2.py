# https://stepik.org/lesson/3369/step/8?unit=952
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4

n = int(input())
separator = ' '
total_count = 0

for i in range(0, n + 1):
    if total_count == n:
        break;

    for j in range(0, i):
        if total_count == n:
            break;

        print(i, end=' ')
        total_count += 1;
