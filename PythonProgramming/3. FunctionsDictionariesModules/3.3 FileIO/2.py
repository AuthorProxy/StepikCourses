# https://stepik.org/lesson/3363/step/3?unit=1135
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3

def calculate_max_entries(data):
    words_dict = {}
    splitted_data = data.lower().split(' ')
    for word in splitted_data:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    max_entries_word = sorted(words_dict.items(), key=lambda x:x[1],  reverse=True)[0]
    return max_entries_word[0] + ' ' + str(max_entries_word[1])

dataset = ''
with open('2.dataset.txt', 'r') as fs:
    dataset += fs.readline().strip()

result = calculate_max_entries(dataset)
with open('2.result.txt', 'w') as fs:
    fs.write(result)

print(result)