# https://stepik.org/lesson/5047/step/4?unit=1086
# Sample Input 1:
# прямоугольник
# 4
# 10
# Sample Output 1:
# 40.0
# Sample Input 2:
# круг
# 5
# Sample Output 2:
# 78.5
# Sample Input 3:
# треугольник
# 3
# 4
# 5
# Sample Output 3:
# 6.0

type = input()
if type == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif type == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif type == 'круг':
    r = float(input())
    print(3.14 * r ** 2)
