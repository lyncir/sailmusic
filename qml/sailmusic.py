# -*- coding: utf-8 -*-
import pyotherside


import os
import io
import logging
from PIL import Image

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
