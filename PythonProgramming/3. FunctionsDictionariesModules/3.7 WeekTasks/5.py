# https://stepik.org/lesson/3380/step/5?unit=963
# Sample Input:
# 6 Вяххи 159
# 11  Федотов 172
# 7 Бондарев  158
# 6 Чайкина 153
# Sample Output:
# 1 -
# 2 -
# 3 -
# 4 -
# 5 -
# 6 156.0
# 7 158.0
# 8 -
# 9 -
# 10 -
# 11 172.0

def calculate_data(data):
    school_dict = {'1': [0, 0], '2': [0, 0], '3': [0, 0], '4': [0, 0], '5': [0, 0], '6': [0, 0], '7': [0, 0], '8': [0, 0], '9': [0, 0], '10': [0, 0], '11': [0, 0]}
    for level, name, grade in data:
        school_dict[level][0] += int(grade)
        school_dict[level][1] += 1
    
    result = []
    for level, [grades, total] in school_dict.items():
        if (total > 0):
            result.append(f'{level} {grades / total}')
        else:
            result.append(f'{level} -')
        
    return result


dataset = []
with open('5.dataset.tsv', 'r') as fs:
    for line in fs.readlines():
        dataset += [line.strip().split('\t')]

result = calculate_data(dataset)
with open('5.result.txt', 'w') as fs:
    fs.writelines("%s\n" % entry for entry in result)

print(result)