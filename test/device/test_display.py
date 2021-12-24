import pytest

from yt_client.device import Display


def test_display():
    d = Display()
    d.hello_world_test()
