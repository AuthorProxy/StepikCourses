# https://stepik.org/lesson/5047/step/3?unit=1086
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

a = float(input())
b = float(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif op == '*':
    print(a * b)
elif op == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif op == 'pow':
    print(a ** b)
elif op == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
