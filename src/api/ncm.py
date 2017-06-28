# -*- coding: utf-8 -*-
import json
import asyncio
import requests
import random
from enum import Enum

from src.api.utils import config, get_url, encrypted_id
from src.api.encrypt import encrypted_request


session = requests.Session()
header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': config()['host'],
    'Referer': 'http://{}'.format(config()['host']),
    'Cookie': 'appver=2.0.2;',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
}


class NCMActions(Enum):
    """
    API接口模板
    """
    # 登录
    LOGIN = '/weapi/login/cellphone?csrf_token='

    # 获取用户歌单
    USER_PLAYLIST = '/api/user/playlist'  # OK

    # 获取歌单内所有音乐
    PLAYLIST_DETAIL = '/api/playlist/detail'  # OK

    # 获取对应音乐的URL
    MUSIC_URL = '/weapi/song/enhance/player/url'  # OK

    # 搜索歌曲
    SEARCH = '/api/search/get'  # OK

    # 获取歌曲详情
    SONG_DETAIL = '/api/song/detail'  # OK

    # 获取专辑内容
    ALBUM = '/api/album/{}'  # OK

    # 私人 FM
    PERSONAL_FM = '/weapi/v1/radio/get'


def get_or_post(method, session, url, data, json, params):
    """
    http请求

    :param method: 请求方式 `GET` or `POST`
    :param session: `requests` 的 `Session` 实例
    :param url: 请求的url
    :param data: post请求时使用的data数据
    :param json: post请求时使用的json数据
    :param params: get请求时使用的参数
    """

    if method == 'POST':
        return session.post(url,
                            data=data,
                            json=json,
                            headers=header,
                            timeout=config()['timeout'])

    elif method == 'GET':
        return session.get(url,
                           params=params,
                           headers=header,
                           timeout=config()['timeout'])


@asyncio.coroutine
def http_request(method, session, url, data=None, json=None, params=None):
    """
    异步requests

    :param method: 请求方式 `GET` or `POST`
    :param session: `requests` 的 `Session` 实例
    :param url: 请求的url
    :param data: post请求时使用的data数据
    :param json: post请求时使用的json数据
    :param params: get请求时使用的参数
    """
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, get_or_post, method, session, url,
                                  data, json, params)
    connection = yield from future

    connection.encoding = 'UTF-8'
    return connection.text


@asyncio.coroutine
def user_playlist(uid, offset=0, limit=10):
    """
    获取用户歌单

    :param uid: 用户id,可通过登录或其它方式获取
    :param offset: 起始位置,默认为0
    :param limit: 数据量,默认10
    """
    url = get_url(NCMActions.USER_PLAYLIST.value)
    params = {"uid": uid,
              "offset": offset,
              "limit": limit}
    connection = yield from http_request('GET', session, url,
                                         params=params)
    result = json.loads(connection)
    return result


@asyncio.coroutine
def playlist_detail(playlist_id):
    """
    获取歌单内所有音乐

    :param playlist_id: 歌单id
    """
    url = get_url(NCMActions.PLAYLIST_DETAIL.value)
    params = {"id": playlist_id}
    connection = yield from http_request('GET', session, url,
                                         params=params)
    result = json.loads(connection)
    return result


@asyncio.coroutine
def music_url(music_id):
    """
    获取对应音乐的URL

    :param music_id: 歌曲id
    """
    url = get_url(NCMActions.MUSIC_URL.value)
    data = {"ids": [music_id],
            "br": 999000,
            "cstf_token": ''}
    data = encrypted_request(data)
    connection = yield from http_request('POST', session, url,
                                         data=data)
    result = json.loads(connection)
    return result


@asyncio.coroutine
def search(s, stype=1, offset=0, limit=10):
    """
    搜索

    :param s: 搜索关键字
    :param stype: 搜索类型，1: 单曲, 100: 歌手, 1000: 歌单, 1002: 用户
    :param offset: 起始位置
    :param limit: 数量
    :param total: 是否显示总数
    """
    url = get_url(NCMActions.SEARCH.value)
    data = {
        's': s,
        'type': stype,
        'offset': offset,
        'limit': limit,
    }
    connection = yield from http_request('POST', session, url,
                                         data=data)
    result = json.loads(connection)
    return result


@asyncio.coroutine
def song_detail(music_id):
    """
    获取歌曲详情

    :param music_id: 歌曲id
    """
    url = get_url(NCMActions.SONG_DETAIL.value)
    params = {"id": music_id,
              "ids": json.dumps([music_id])}
    connection = yield from http_request('GET', session, url,
                                         params=params)
    result = json.loads(connection)
    return result


@asyncio.coroutine
def album(album_id):
    """
    获取专辑内容

    :param album_id: 专辑id
    """
    url = get_url(NCMActions.ALBUM.value.format(album_id))
    connection = yield from http_request('GET', session, url)
    result = json.loads(connection)
    return result
