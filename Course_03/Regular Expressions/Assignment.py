import re

sample_text = '1an apple 2 is taken 3 5 5434 Aby baby'

res = re.findall('[a-z0-9]',sample_text)

print(res)