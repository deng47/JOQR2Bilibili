#!/usr/bin/env python3

import os
import requests
import re
from bs4 import BeautifulSoup
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description = "A command line tool search Bilibili vedio")
    parser.add_argument(
        "--aid", required = True)
    return parser.parse_args()

def main():
    args = parse_args()
    aid = args.aid
    link = 'https://www.bilibili.com/video/av'
    working_dir = '/project/radio'

    with open('%s/cookie' % working_dir) as f:
        cookie = f.read()[:-1]

    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36', 'cookie':cookie}
    response = session.get(link+aid, headers=headers)
    html = response.text
    cid = re.search('"cid":(.*?),', html).group(1)
    print(cid)

if __name__ == '__main__':
    main()
