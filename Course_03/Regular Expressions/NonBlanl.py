
import re

text = 'srimanikantapalakollu@gmail.com'

res = re.findall('@(.\S*)',text)

print(res)