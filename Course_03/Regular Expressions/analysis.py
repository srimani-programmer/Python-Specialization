import re

file_handle = open('mbox-test.txt')

# Extracting the Dates from the text file.

for data in file_handle:
    lines = data.strip()
    if re.search('^Date:',lines):
        print(lines)

file_handle.close()