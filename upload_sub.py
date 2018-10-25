#!/usr/bin/env python3

import requests
import re
import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description = "A command line tool upload sub file to Bilibili")
    parser.add_argument(
        "--sub", required = True)
    parser.add_argument(
        "--aid", required = True)
    parser.add_argument(
        "--cid", required = True)
    return parser.parse_args()

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
        self.session.headers['Host'] = 'api.bilibili.com'

    def upload_sub(self, aid, cid, json_data):
        form_data={
        'data':json_data,
        'aid':aid,
        'csrf':self.csrf,
        'submit':'true',
        'sign':'true',
        'lan':'ja',
        'oid':cid,
        'type':'1'}
        response = self.session.post(self.link, 
            headers = self.session.headers,
            data = form_data
            )
        print(response.text)


def main():
    working_dir = '/project/radio'
    args = parse_args()
    aid = args.aid
    cid = args.cid
    sub = args.sub

    with open('%s/cookie' % working_dir) as f:
        cookie = f.read()[:-1]
    with open(sub) as f:
        lines = f.readlines()
        sub_data = lines[0] + ','.join(lines[1:-1]) + lines[-1]
        json_data = sub_data.replace('\n','')

    b = Bilibili(cookie)
    b.upload_sub(aid, cid, json_data)

if __name__ == '__main__':
    main()
