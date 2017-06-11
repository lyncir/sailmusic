# -*- coding: utf-8 -*-
import asyncio
import requests

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
    result = loop.run_utils_complete(login(username, password))
    loop.close()


if __name__ == '__main__':
    main()
