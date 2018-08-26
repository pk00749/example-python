# -*- coding:utf-8 -*-
# encoding: utf-8
#import requests
import urllib
import urllib2
import re
import os


url_1 = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1472289365626_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1472289365627%5E00_1423X775&word='
keyWords = raw_input(r"输入关键字:")

url = url_1+urllib.quote(keyWords)

dirPath = r'F:\img'
subPath = unicode(os.path.join(dirPath, keyWords),'utf-8')


request = urllib2.Request(url)
response = urllib2.urlopen(request)
pattern = re.compile(r'"objURL":"(.*?)"', re.S)
content = response.read().decode('utf-8')

urls = re.findall(pattern, content)

if not os.path.isdir(subPath): #dirPath
    os.mkdir(subPath)

index = 1
for url in urls:
    print("Downloading:", url)
    try:
        filename = os.path.join(subPath, str(index) + ".jpg")
        u = urllib.urlopen(url)
        data = u.read()
        content = response.read().decode('utf-8')

        with open(filename, 'wb') as f:
            f.write(data)
            index += 1

    except urllib2.URLError, error:  # The parent of HTTPError is URLError
        if hasattr(error, "code"):
            print error.code
        if hasattr(error, "reason"):
            print error.reason
    else:
        print "Success"

print("Done,total %s" % index)