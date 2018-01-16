#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

BASE_URL='http://sports.qq.com/nba/'
usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
        }
def getWebHtmlConent():
    source = requests.get(BASE_URL,usr_agent)
    soup = BeautifulSoup(source.content,'html.parser')
    results = soup.find_all("a")
    print soup.get_text()
    for link in results:
        print link.get('href'),link.get_text()

getWebHtmlConent()