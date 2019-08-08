import urllib.error, urllib.request
from bs4 import BeautifulSoup

url = input('Enter Url:')
count = int(input('Enter count:'))
position = int(input('Enter position:') )
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

tags = soup('a')
my_tags = tags[position-1]
needed_tag = my_tags.get('href', None)
print("------ : ", tags[position-1].contents[0])

for x in range(count-1):

    url = str(needed_tag)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    print("------ : ", tags[position-1].contents[0])