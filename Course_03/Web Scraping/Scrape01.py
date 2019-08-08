import requests
from bs4 import BeautifulSoup

req = requests.get('http://py4e-data.dr-chuck.net/comments_42.html')

soup = BeautifulSoup(req.text, 'lxml')

data = soup.find_all('span', class_="comments")

totalSum = 0
for i in data:
    val = int(i.text)
    totalSum += val

print(totalSum)