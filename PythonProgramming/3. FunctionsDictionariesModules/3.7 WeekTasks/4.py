# https://stepik.org/lesson/3380/step/4?unit=963
# Sample Input:
# 4
# север 10
# запад 20
# юг 30
# восток 40
# Sample Output:
# 20 -20

napr = {'север': (0, 1), 'запад': (-1, 0), 'юг': (0, -1), 'восток': (1, 0)}
n = int(input())
x_list = [(input()).split(' ') for x in range(n)]
dvizh = [(napr[x][0]*int(y), napr[x][1]*int(y)) for x, y  in x_list]
res = (sum([x for x, y in dvizh]), sum([y for x, y in dvizh]))
print(' '.join(map(str, res)))
