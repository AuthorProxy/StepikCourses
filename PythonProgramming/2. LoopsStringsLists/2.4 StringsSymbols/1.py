# https://stepik.org/lesson/3367/step/3?unit=950
# Sample Input:
# acggtgttat
# Sample Output:
# 40.0

str = input().upper()
print((str.count('G') + str.count('C')) / len(str) * 100)
