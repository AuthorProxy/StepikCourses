# https://stepik.org/lesson/2414/step/5?unit=931
# Sample Input 1:
# 6
# 10
# 8
# Sample Output 1:
# Это нормально
# Sample Input 2:
# 7
# 9
# 10
# Sample Output 2:
# Пересып
# Sample Input 3:
# 7
# 9
# 2
# Sample Output 3:
# Недосып

min_sleep_time = int(input())
max_sleep_time = int(input())
sleep_time = int(input())

if sleep_time < min_sleep_time:
    print('Недосып')
elif sleep_time > max_sleep_time:
    print('Пересып')
else:
    print('Это нормально')
