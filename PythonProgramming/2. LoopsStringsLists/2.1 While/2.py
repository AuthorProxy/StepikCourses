# https://stepik.org/lesson/3364/step/12?unit=947
# Sample Input 1:
# 1
# 2
# Sample Output 1:
# 2
# Sample Input 2:
# 7
# 5
# Sample Output 2:
# 35
# Sample Input 3:
# 15
# 15
# Sample Output 3:
# 15

a, b = int(input()), int(input())

def GCD(x,y):
  return x if y == 0 else GCD(y,x%y)

def LCM(x,y):
  return x*y / GCD(x,y)

print(int(LCM(a,b)))
