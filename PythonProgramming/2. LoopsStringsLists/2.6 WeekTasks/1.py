# https://stepik.org/lesson/3369/step/7?unit=952
# Sample Input:
# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# Sample Output:
# 340

summ = 0
array = []
while(len(array) == 0 or summ != 0):
    x = int(input())
    array.append(x)
    summ += x

print(sum([i*i for i in array]))
