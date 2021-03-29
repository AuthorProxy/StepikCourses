# https://stepik.org/lesson/3378/step/3?unit=961

import requests

base_url = 'https://stepik.org/media/attachments/course67/3.6.3/'
def request_data(url):
    r = requests.get(url)
    print(r.status_code, url)

    if r.status_code == 200:
        return request_data(base_url + r.text.strip())
    
    return url.replace(base_url, '')
    

dataset = ''
with open('2.dataset.txt', 'r') as fs:
    dataset = fs.readline().strip()

result = request_data(dataset)
with open('2.result.txt', 'w') as fs:
    fs.write(result)

print(result)