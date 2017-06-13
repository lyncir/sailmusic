# -*- coding: utf-8 -*-
import os
import re
import time
import asyncio
import requests
import traceback
from http.cookiejar import LWPCookieJar

import utils


header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'http://music.163.com/search/',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'  # NOQA
}

timeout = 10
cookies = {'appver': '1.5.2'}
session = requests.Session()
cookie_path = "cookie"
session.cookies = LWPCookieJar(cookie_path)

try:
    session.cookies.load()
    cookie = ''
    if os.path.isfile(cookie_path):
        f = open(cookie_path, 'r')
        cookie = f.read()
        f.close()
    expire_time = re.compile(r'\d{4}-\d{2}-\d{2}').findall(cookie)
    if expire_time:
        if expire_time[0] < time.strftime('%Y-%m-%d', time.localtime(time.time())):
            os.remove(cookie_path)
except IOError as e:
    print(traceback.format_exc())
    session.cookies.save()


# 登录
@asyncio.coroutine
def login(username, password):
    action = 'https://music.163.com/weapi/login?csrf_token='
    text = {
        'username': username,
        'password': password,
        'rememberLogin': 'true'
    }
    data = utils.encrypted_request(text)
    connection = session.post(action,
                              data=data,
                              headers=header,
                              timeout=timeout)
    print(connection, type(connection))
    print(connection.text)


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(login(username, password))
    loop.close()


if __name__ == '__main__':
    main()
