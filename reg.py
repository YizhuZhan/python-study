# -*- coding:utf-8 -*-

import urllib.request as request
import re


"""
    抓取图片到本地：1.抓取网页； 2.获取图片地址； 3.抓取图片存到本地
"""
req = request.urlopen('http://www.imooc.com/course/list')
buf = req.read().decode('utf-8')  # 将bytes解码为utf-8字符串
listurl = re.findall(r'//img.+?\.jpg', buf)
result = [url.replace('//', 'http://') for url in listurl]
print(len(result), result)
i = 0
for url in result:
    f = open(str(i) + '.jpg', 'wb+')  # wb+方式支持二进制写入
    _req = request.urlopen(url)
    _buf = _req.read()
    f.write(_buf)
    i += 1
    f.close()


