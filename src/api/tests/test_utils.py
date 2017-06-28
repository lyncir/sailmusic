# -*- coding: utf-8 -*-
import pytest

from src.api.utils import config


def test_config():
    """
    测试配置文件读取
    """
    result = config()
    assert result['host'] == 'music.163.com'
    assert result['timeout'] == 10
    assert result['music_quality'] == 0
