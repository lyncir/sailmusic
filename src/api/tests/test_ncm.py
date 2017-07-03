# -*- coding: utf-8 -*-
import pytest
import json

from src.api.ncm import song_detail, search, user_playlist, \
    playlist_detail, album, music_url


def test_user_playlist(loop):
    """
    获取用户歌单
    """
    result = loop.run_until_complete(user_playlist('36554272',
                                                   limit=1))
    assert result['code'] == 200


def test_playlist_detail(loop):
    """
    获取歌单内所有音乐
    """
    result = loop.run_until_complete(playlist_detail('721974886'))
    assert result['code'] == 200
    assert result['result']['trackCount'] == 4  # 4首歌曲


def test_music_url(loop):
    result = loop.run_until_complete(music_url('347230'))
    assert result['code'] == 200
    assert result['data'][0]['md5'] == '5d64960d0cbebc0d089bc85a6ef54680'


def test_search(loop):
    """
    搜索
    """
    result = loop.run_until_complete(search('gravityWall',
                                            limit=1))
    assert result['code'] == 200  # 正常返回
    assert result['result']['songCount'] == 12  # 搜索到7首


def test_song_detail(loop):
    """
    歌曲明细
    """
    result = loop.run_until_complete(song_detail(482999012))
    assert result['code'] == 200  # 正常返回
    assert len(result['songs']) == 1  # 一首歌曲
    assert result['songs'][0]['id'] == 482999012  # 歌曲id相同


def test_album(loop):
    """
    获取专辑内容
    """
    result = loop.run_until_complete(album('2525474'))
    assert result['code'] == 200
    assert result['album']['size'] == 12  # 专辑包含12首歌曲
