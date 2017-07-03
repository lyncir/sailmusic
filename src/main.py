# -*- coding: utf-8 -*-
import os
import io
import socket
import fcntl
import struct
import asyncio
import logging
import traceback

import pyotherside
from PIL import Image

from api import ncm


logging.basicConfig(filename='/tmp/sailmusic.log', level=logging.DEBUG)


def render(image_id, requested_size):
    logging.info('image_id: "{image_id}", size: {requested_size}'.format(**locals()))

    # width and height will be -1 if not set in QML
    if requested_size == (-1, -1):
        requested_size = (300, 300)

    filename = os.path.join(os.path.dirname(__file__), 'images', image_id)
    logging.info(filename)
    with open(filename, "rb") as f:
        data = bytearray(f.read())

    img = Image.open(io.BytesIO(data))

    return data, img.size, pyotherside.format_data


pyotherside.set_image_provider(render)


def get_ip_address(ifname):
    """
    获取接口的ip地址

    :param ifname: 网络接口名
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_addr = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR 获取接口地址
            struct.pack('256s', ifname[:15])
        )[20:24])
    except OSError as e:
        if e.errno == 19:
            ip_addr = 'Device Not Found'
        elif e.errno == 99:
            ip_addr = 'Disconnected'
        else:
            ip_addr = 'OSError'
    except:
        ip_addr = 'Error. See log!'
        logging.info(traceback.format_exc())
    return ip_addr


pyotherside.send("ip_address", get_ip_address(b"wlan0"))


def get_music_url(music_id):
    """
    获取音乐的url
    """
    try:
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(ncm.music_url(music_id))
        loop.close()
    except:
        logging.info(traceback.format_exc())
    logging.info(result)
    return result['data'][0]['url']


pyotherside.send("music_url", get_music_url('347230'))


if __name__ == '__main__':
    print(get_ip_address(b"wlan0"))
