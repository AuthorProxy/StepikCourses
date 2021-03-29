# https://stepik.org/lesson/3373/step/5?unit=956
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key*2 in d:
        d[key*2].append(value)
    else:
        d[key*2]=[value]

# не добавляйте кода вне функции
