# https://stepik.org/lesson/3372/step/8?unit=955
# Sample Input 1:
# 4.5
# Sample Output 1:
# 7.25
# Sample Input 2:
# -4.5
# Sample Output 2:
# -5.25
# Sample Input 3:
# 1
# Sample Output 3:
# -0.5

def f(x):
    if x <= -2:
        return 1-(x+2)**2
    if -2 < x <= 2:
        return -x/2
    if x > 2:
        return (x-2)**2+1
