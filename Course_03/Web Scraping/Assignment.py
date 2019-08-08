import urllib.request 
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_190244.html').read()

soup = BeautifulSoup(req, 'lxml')

data = soup.find_all('span', class_="comments")

totalSum = 0
for i in data:
    val = int(i.text)
    totalSum += val

print(totalSum)