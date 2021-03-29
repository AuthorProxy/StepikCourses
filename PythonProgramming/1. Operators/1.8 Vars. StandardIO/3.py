# https://stepik.org/lesson/2232/step/8?unit=929
# Sample Input 1:
# 480
# 1
# 2
# Sample Output 1:
# 9
# 2
# Sample Input 2:
# 475
# 1
# 55
# Sample Output 2:
# 9
# 50

total_minutes = int(input())
go_sleep_at_hour = int(input())
go_sleep_at_minute = int(input())
go_sleep_at_total_minutes = go_sleep_at_hour * 60 + go_sleep_at_minute

time_to_wakeup_total_minutes = go_sleep_at_total_minutes + total_minutes
wakeup_at_hours = time_to_wakeup_total_minutes // 60
wakeup_at_minutes = time_to_wakeup_total_minutes % 60

print(wakeup_at_hours)
print(wakeup_at_minutes)
