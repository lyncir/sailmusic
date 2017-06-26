# -*- coding: utf-8 -*-
import pytest
import asyncio


@pytest.fixture
def loop():
    # set up
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop

    # clean up
    loop.close()
