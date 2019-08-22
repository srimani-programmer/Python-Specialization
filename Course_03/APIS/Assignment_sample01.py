from urllib.request import urlopen
import json

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
req = urlopen(url).read()

jsonHandler = json.loads(req)

dataList = jsonHandler['comments']

total_sum = 0

for i in dataList:
    total_sum += int(i['count'])

print(total_sum)