# https://stepik.org/lesson/3363/step/2?unit=1135
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb

def print_letters(letter, repeats):
    return [letter for x in range(int(repeats))]

def decipher(str):
    letter = ''
    repeats = ''
    result = []
    for sym in str:
        if sym in '0123456789':
            repeats += sym
        elif repeats:
            result += print_letters(letter, repeats)
            repeats = ''
            letter = sym
        else:
            letter = sym
    
    result += print_letters(letter, repeats)
    return ''.join(result)

dataset = ''
with open('1.dataset.txt', 'r') as fs:
    dataset += fs.readline().strip()

result = decipher(dataset)
with open('1.result.txt', 'w') as fs:
    fs.write(result)

print(result)