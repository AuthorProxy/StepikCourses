# https://stepik.org/lesson/5047/step/6?unit=1086
# Sample Input 1:
# 5
# Sample Output 1:
# 5 программистов
# Sample Input 2:
# 0
# Sample Output 2:
# 0 программистов
# Sample Input 3:
# 1
# Sample Output 3:
# 1 программист
# Sample Input 4:
# 2
# Sample Output 4:
# 2 программиста

n = int(input())
result = str(n) + ' программист'
if n % 10 == 0 or 5 <= n % 10 < 10 or 10 < n % 100 < 15: result += 'ов'
elif 1 < n % 10 < 5: result += 'а'
print(result)
