# https://stepik.org/lesson/5047/step/7?unit=1086
# Sample Input 1:
# 090234
# Sample Output 1:
# Счастливый
# Sample Input 2:
# 123456
# Sample Output 2:
# Обычный

ticket = int(input())
a6 = ticket % 10
ticket //= 10
a5 = ticket % 10
ticket //= 10
a4 = ticket % 10
ticket //= 10
a3 = ticket % 10
ticket //= 10
a2 = ticket % 10
ticket //= 10
a1 = ticket % 10

if a1 + a2 + a3 == a4 + a5 + a6: print("Счастливый")
else: print("Обычный")
