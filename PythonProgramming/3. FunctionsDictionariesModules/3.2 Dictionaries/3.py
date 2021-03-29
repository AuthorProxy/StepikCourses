# https://stepik.org/lesson/3373/step/7?unit=956
# Sample Input:
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
# 11
# 41
# 47
# 61
# 41

# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
result = {}
key = 0

for i in range(0,n):
    key = int(input())
    if key not in result:
        result[key] = f(key)
    print(result[key])
