import re

file_handle = open('mbox-test.txt')

# Printing the data starts with 'x'
count = 0
for data in file_handle:
    lines = data.strip()
    if re.search('^X.*:',lines):
       # print(data)
       count += 1

print(count)


file_handle.close()