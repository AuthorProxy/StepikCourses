# https://stepik.org/lesson/3372/step/9?unit=955
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

def modify_list(l):
    temp = list(l)
    del l[:]
    for i in temp:
        if i%2==0:
            l.append(i//2)
