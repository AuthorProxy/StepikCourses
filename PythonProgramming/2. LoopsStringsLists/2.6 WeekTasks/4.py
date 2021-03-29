# https://stepik.org/lesson/3369/step/10?unit=952
# Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1
# Sample Input 2:
# 1
# end
# Sample Output 2:
# 4

matrix = []
inp = input()
while inp != 'end':
    matrix.append([int(i) for i in inp.split()])
    inp = input()

matr_len_str = len(matrix[0])
matr_len_col = len(matrix)

result = []
for i in range(matr_len_col):
    temp_sum = 0
    temp_row = []
    for j in range(matr_len_str):
        iandone = i+1
        jandone = j+1

        if (iandone >= matr_len_col):
            iandone = 0;

        if (jandone >= matr_len_str):
            jandone = 0;

        temp_sum = matrix[i-1][j] + matrix[iandone][j] + matrix[i][j-1] + matrix[i][jandone]
        temp_row.append(temp_sum)
    result.append(temp_row)


for i in range(matr_len_col):
    for j in range(matr_len_str):
        print(result[i][j], end=' ')
    print()
