# -*- coding: utf-8 -*-
import pytest

from src.api.ncm import song_detail, search


def test_search(loop):
    """
    搜索
    """
    result = loop.run_until_complete(search('gravityWall'))
    assert result['code'] == 200  # 正常返回
    assert result['result']['songCount'] == 7  # 搜索到7首


def test_song_detail(loop):
    """
    歌曲明细
    """
    result = loop.run_until_complete(song_detail(482999012))
    assert result['code'] == 200  # 正常返回
    assert len(result['songs']) == 1  # 一首歌曲
    assert result['songs'][0]['id'] == 482999012  # 歌曲id相同
