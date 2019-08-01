import re

file_handle = open('Actualdata.txt')
number_list = list()

for data in file_handle:
    data = data.strip()
    temp = re.findall('[0-9]+',data)
    for i in temp:
        number_list.append(i)

sum_value = 0

for i in number_list:
    sum_value += int(i)


# Printing the Final Result
print(sum_value)
