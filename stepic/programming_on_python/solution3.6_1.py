# pip install requests
import requests

# TODO use unique dataset ***.txt
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/685.txt')
count = 0
for i in r.text.splitlines():
    count += 1
print(count)
