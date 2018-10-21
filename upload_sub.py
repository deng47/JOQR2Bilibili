#!/usr/bin/env python3

import requests
import re
import json

class Bilibili:
    def __init__(self, cookie):
        self.session = requests.session()
        self.session.headers['Cookie'] = cookie
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        self.link = 'https://api.bilibili.com/x/v2/dm/subtitle/draft/save'
        self.csrf = re.search('bili_jct=(.*?);', cookie).group(1)
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.session.headers['Referer'] = 'https://account.bilibili.com/subtitle/edit/'
        self.session.headers['Host'] = 'api.bilibili.com'
        self.session.headers['Origin'] = 'https://account.bilibili.com'
        self.session.headers['Accept'] = 'application/json, text/plain, */*'
        self.session.headers['Accept-Encoding'] = 'gzip, deflate, br'
        self.session.headers['Accept-Language'] = 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7'
        self.session.headers['Connection'] = 'keep-alive'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        #self.session.headers['X-Hola-Request-Id'] = '31145947'
        #self.session.headers['X-Hola-Unblocker-Bext'] = 'reqid 31145947: before request, send headers'
        #self.session.headers['Content-Length'] = '290598'

    def upload_sub(self, aid, json_data):
        json_data = json.loads(json_data)

        response = self.session.post(self.link, data={
            'data':json_data,
            'aid':aid,
            'csrf':self.csrf,
            'submit':'true',
            'lan':'en',
            'oid': 59646760,
            'type':1
            },
            headers = self.session.headers)
        print(response.text)
        print(response.request.headers)



aid = '34005386' # https://www.bilibili.com/video/av34005386/
working_dir = '/project/radio'

with open('%s/cookie' % working_dir) as f:
    cookie = f.read()[:-1]

with open('%s/json' % working_dir) as f:
    lines = f.readlines() 
    json_data = lines[0] + ','.join(lines[1:-1]) + lines[-1]

b = Bilibili(cookie)
b.upload_sub(aid, json_data)

