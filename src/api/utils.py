# -*- coding: utf-8 -*-
import os
import yaml
import urllib


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
