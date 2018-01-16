#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print 'hello,world'
import requests
import math
import simple


def sendRequst():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    headers = {'User-Agent', user_agent}
    r = requests.get("http://www.qiushibaike.com/hot/page/2/",headers)
    print r.url,r.status_code
    return r.status_code
sendRequst()

content=dir(math)
print(content)

simple.simple()

str=raw_input('input')
print(str)
