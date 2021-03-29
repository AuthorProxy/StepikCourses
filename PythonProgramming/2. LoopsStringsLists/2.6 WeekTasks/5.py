# https://stepik.org/lesson/3369/step/11?unit=952
# Sample Input:
# 5
# Sample Output:
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

def position(a):
    x = 0
    y = 0
    minX, maxX = 1, a - 1
    minY, maxY = 0, a - 1
    xyz = 1
    for count in range(1, a**2 + 1, 1):
        yield x, y
        if xyz == 1:
            y += 1
            if y == maxY:
                xyz +=1
                maxY -=1
        elif xyz == 2:
            x += 1
            if x == maxX:
                xyz +=1
                maxX -=1
        elif xyz == 3:
            y -= 1
            if y == minY:
                xyz +=1
                minY +=1
        elif xyz == 4:
            x -= 1
            if x == minX:
                xyz +=1
                minX +=1
        if xyz > 4:
            xyz = 1

def PrintHelix(z):
    a = len(z)
    for x in range(a):
        row = ""
        for y in range(a):
            row += " " + z[x][y]
        print (row)

a = int(input())
z = [[0]*a for x in range(a)]
for index, (x,y) in enumerate(position(a), 1):
    z[x][y] = str(index)

PrintHelix(z)
