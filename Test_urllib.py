#-*-coding=utf-8-*-
import re
import urllib.request as ur
from bs4 import BeautifulSoup

url = "http://www.huya.com/g/"
# data = urllib.urlopen(url).read()
data = ur.urlopen(url)
print('http header: \n', data.info())
print('http status:', data.getcode())
print('url:', data.geturl())
print(data.read().decode('utf-8'))
soup = BeautifulSoup(data, 'html.parser').findAll("ul")
href = re.findall(""".*?href="(.*?)".*""", str(data))
# f = open('D:\desktop\\a.txt', 'a+')
# f.write(data)
# f.close()

# print data
# print data.info()
