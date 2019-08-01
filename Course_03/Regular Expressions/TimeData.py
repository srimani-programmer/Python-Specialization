import re

file_handle = open('mbox-test.txt')
time_data = list()

for data in file_handle:
    data = data.strip()
    temp = re.findall('[0-9]+:[0-9]+:[0-9]+ [0-9]+',data)
    for timeValue in temp:
        time_data.append(timeValue)
    

for i in time_data:
    print(i)

file_handle.close()

