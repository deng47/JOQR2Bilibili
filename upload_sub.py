#!/usr/bin/env python3

import requests
import re
import json

class Bilibili:
    def __init__(self, cookie):
        self.session = requests.session()
        self.session.headers['cookie'] = cookie
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        self.link = 'https://api.bilibili.com/x/v2/dm/subtitle/draft/save'
        self.csrf = re.search('bili_jct=(.*?);', cookie).group(1)
        self.session.headers['Accept'] = 'application/json, text/plain, */*'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.session.headers['Referer'] = 'https://account.bilibili.com/subtitle/edit/'
        self.session.headers['Origin'] = 'https://account.bilibili.com'

    def upload_sub(self, aid, json_data):
        print(type(json_data))
        print(json_data)
        form_data={
        'data':json_data,
        'aid':aid,
        'csrf':self.csrf,
        'submit':'true',
        'sign':'false',
        'lan':'ko',
        'oid':'59646760',
        'type':'1'}
        response = self.session.post(self.link, 
            headers = self.session.headers,
            data = form_data
            )
        print(response.text)



aid = '34055284' # https://www.bilibili.com/video/av34055284/
working_dir = '/project/radio'

with open('%s/cookie' % working_dir) as f:
    cookie = f.read()[:-1]

with open('%s/json' % working_dir) as f:
    lines = f.readlines()
    sub_data = lines[0] + ','.join(lines[1:-1]) + lines[-1]
    json_data = sub_data.replace('\n','')

b = Bilibili(cookie)
b.upload_sub(aid, json_data)

