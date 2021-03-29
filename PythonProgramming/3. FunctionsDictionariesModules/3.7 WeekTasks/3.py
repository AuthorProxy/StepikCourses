# https://stepik.org/lesson/3380/step/3?unit=963
# Sample Input:
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
# stepic
# champignons
# the

n = int(input())
words = []

for i in range(0,n):
    words.append(input().strip().lower())


n = int(input())
strs_dict = set()

for i in range(0,n):
    inp = input().strip().lower().split(" ")
    for i in inp:
        strs_dict.add(i)

for i in words:
    strs_dict.discard(i)

for i in strs_dict:
    print(i)
