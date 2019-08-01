import re

file_handle = open('mbox-test.txt')

numbers_data = list()
for data in file_handle:
    lines = data.strip()
    if re.search('[0-9]',lines):
        numbers_data.append(re.findall('[0-9]+',lines))

# print(len(numbers_data.shape))

print(numbers_data)

file_handle.close()