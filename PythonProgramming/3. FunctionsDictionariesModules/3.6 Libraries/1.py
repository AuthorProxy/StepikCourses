# https://stepik.org/lesson/3378/step/1?unit=961

import requests

def calculate_lines(data):
    return str(len(data.splitlines()))

def request_data(url):
    return requests.get(url).text
    

dataset = ''
with open('1.dataset.txt', 'r') as fs:
    dataset = fs.readline().strip()

text = request_data(dataset)
result = calculate_lines(text)
with open('1.result.txt', 'w') as fs:
    fs.write(result)

print(result)