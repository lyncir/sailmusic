# -*- coding: utf-8 -*-
import pytest

from src.api.utils import config


def test_config():
    """
    测试配置文件读取
    """
    result = config()
    assert result == {'url': 'http://music.163.com'}
