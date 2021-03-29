# https://stepik.org/lesson/3363/step/4?unit=1135
# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

def calculate_students_performance(data):
    result = [str((int(grade1) + int(grade2) + int(grade3)) / 3) for name, grade1, grade2, grade3 in data]
    averageGrade1 = sum([int(grade1) for name, grade1, grade2, grade3 in data]) / len(data)
    averageGrade2 = sum([int(grade2) for name, grade1, grade2, grade3 in data]) / len(data)
    averageGrade3 = sum([int(grade3) for name, grade1, grade2, grade3 in data]) / len(data)
    return result + [str(averageGrade1) + ' ' + str(averageGrade2) + ' ' + str(averageGrade3)]

dataset = []
with open('3.dataset.txt', 'r') as fs:
    for line in fs.readlines():
        dataset += [line.strip().split(';')]

result = calculate_students_performance(dataset)
with open('3.result.txt', 'w') as fs:
    fs.writelines("%s\n" % entry for entry in result)

print(result)