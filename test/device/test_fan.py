import pytest
from time import sleep

from yt_client.device import Fan


def test_fan():
    f = Fan()
    f.set_speed(100)
    sleep(1)
