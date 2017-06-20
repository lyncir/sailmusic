# -*- coding: utf-8 -*-
import json
import asyncio
import requests


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
session = requests.Session()


@asyncio.coroutine
def http_request(method, session, url, data=None, **kwargs):
    loop = asyncio.get_event_loop()
    if method == 'POST':
        future = loop.run_in_executor(None, session.post, url, data, kwargs)
        connection = yield from future

    elif method == 'GET':
        future = loop.run_in_executor(None, session.get, url)
        connection = yield from future

    connection.encoding = 'UTF-8'
    return connection.text


# 搜索单曲(1)，歌手(100)，专辑(10)，歌单(1000)，用户(1002) *(type)*
@asyncio.coroutine
def search(s, stype=1, offset=0, total='true', limit=60):
    action = 'http://music.163.com/api/search/get'
    data = {
        's': s,
        'type': stype,
        'offset': offset,
        'total': total,
        'limit': limit
    }
    connection = yield from http_request('POST',
                                         session,
                                         action,
                                         data=data,
                                         headers=header,
                                         timeout=timeout)

    result = json.loads(connection)
    return result


@asyncio.coroutine
def song_detail(music_id):
    action = 'http://music.163.com/api/song/detail/?id={}&ids=[{}]'.format(
            music_id, music_id)
    connection = yield from http_request('GET',
                                         session,
                                         action)
    print(connection)
    print(type(connection))
    result = json.loads(connection)
    return result


def main():
    loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(login(username, password))
    result = loop.run_until_complete(song_detail(482999012))
    loop.close()


if __name__ == '__main__':
    main()
