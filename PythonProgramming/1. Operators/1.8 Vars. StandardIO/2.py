# https://stepik.org/lesson/2232/step/7?unit=929
# Sample Input 1:
# 480
# Sample Output 1:
# 8
# 0
# Sample Input 2:
# 512
# Sample Output 2:
# 8
# 32

total_minutes = int (input())
hours_to_sleep = total_minutes // 60
minutes_to_sleep = total_minutes % 60
print(hours_to_sleep)
print(minutes_to_sleep)
