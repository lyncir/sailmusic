# -*- coding: utf-8 -*-
import pytest
import asyncio


@pytest.fixture
def loop():
    loop = asyncio.get_event_loop()
    return loop
