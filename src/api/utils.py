# -*- coding: utf-8 -*-
import os
import yaml
import urllib
import hashlib
import base64


# 当前目录
_basedir = os.path.abspath(os.path.dirname(__file__))


def config():
    """
    加载配置文件
    """
    file_path = os.path.join(_basedir, 'config.yml')
    with open(file_path, 'rb') as f:
        return yaml.load(f.read())


def get_url(uri):
    """
    拼接url

    :param uri: api接口地址
    """
    return urllib.parse.urljoin("http://{}".format(config()['host']), uri)


def encrypted_id(id):
    """
    歌曲加密算法, 基于https://github.com/yanunon/NeteaseCloudMusic脚本实现

    :param id: 歌曲id
    """
    magic = bytearray('3go8&$8*3*3h0k(2)2', 'u8')
    song_id = bytearray(id, 'u8')
    magic_len = len(magic)
    for i, sid in enumerate(song_id):
        song_id[i] = sid ^ magic[i % magic_len]
    m = hashlib.md5(song_id)
    result = m.digest()
    result = base64.b64encode(result)
    result = result.replace(b'/', b'_')
    result = result.replace(b'+', b'-')
    return result.decode('utf-8')
