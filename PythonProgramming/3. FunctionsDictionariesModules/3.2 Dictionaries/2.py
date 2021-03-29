# https://stepik.org/lesson/3373/step/6?unit=956
# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

s = input()
words = s.strip().lower().split(" ")
temp_hash = {}

for i in words:
    if i in temp_hash:
        temp_hash[i] += 1
    else:
        temp_hash[i] = 1

for k, v in temp_hash.items():
    print(k, v, sep=" ")
