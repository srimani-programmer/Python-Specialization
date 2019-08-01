import re

with open('mbox-test.txt') as f:
    for i in f:
        i = i.strip()
        if(re.search('^Mime.*:', i)):
            print(i)