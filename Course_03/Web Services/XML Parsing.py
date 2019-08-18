import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup

req = urlopen('http://py4e-data.dr-chuck.net/comments_42.xml').read()


xml_handle = ET.fromstring(req)

sub_tag = xml_handle.findall('comments/comment')

totalsum = 0

for i in sub_tag:
    totalsum += int(i.find('count').text)

print(totalsum)