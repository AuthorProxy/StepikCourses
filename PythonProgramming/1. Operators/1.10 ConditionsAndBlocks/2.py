# https://stepik.org/lesson/2414/step/6?unit=931
# Sample Input 1:
# 2100
# Sample Output 1:
# Обычный
# Sample Input 2:
# 2000
# Sample Output 2:
# Високосный

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
