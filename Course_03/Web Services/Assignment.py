import xml.etree.ElementTree as ET
from urllib.request import urlopen


req = urlopen('http://py4e-data.dr-chuck.net/comments_190246.xml').read()


xml_handle = ET.fromstring(req)

sub_tag = xml_handle.findall('comments/comment')

totalsum = 0

for i in sub_tag:
    totalsum += int(i.find('count').text)

print(totalsum)