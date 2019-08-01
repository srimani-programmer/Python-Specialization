import re

with open('mbox-test.txt') as f:

    for i in f:
        i = i.strip()

        if(re.search('^component',i)):
            print(i)