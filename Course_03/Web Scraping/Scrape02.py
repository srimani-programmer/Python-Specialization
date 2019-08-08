import requests
from bs4 import BeautifulSoup

req = requests.get('http://py4e-data.dr-chuck.net/known_by_Fikret.html')

soup = BeautifulSoup(req.text, 'lxml')

link = soup.find_all('a')

names_list = list()
count = 0
new_url = None
for i in link:
    if(count == 3):
        new_url = i['href']
        names_list.append(i.text)
        break
    count += 1
print(new_url, names_list)