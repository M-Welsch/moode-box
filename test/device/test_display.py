import pytest
from time import sleep

from yt_client.device import Display


def test_display():
    d = Display()
    d.hello_world_test()
    sleep(1)
    for line in [1, 2, 3, 4, 5, 6]:
        if line == 1:
            text = "abcdefghijklmnopqrstuvwxyz"
        else:
            text = f"line {line}"
        d.write_text(line, text)
