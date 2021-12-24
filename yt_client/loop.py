from time import sleep

from yt_client.common import Info
from yt_client.common.visualisation import Visualisation
from yt_client.device import Display, Fan


class Loop:
    def __init__(self):
        self._info = Info()
        self._display = Display()
        self._fan = Fan()
        self._vis = Visualisation(self._info)

    def start(self):
        while True:
            self._fan.set_speed(100)
            self._display.clear()
            self._vis.update_sysinfo()
            for index, line in enumerate(self._vis.screen1()):
                self._display.write_text(index+1, line)
            sleep(5)
            self._display.clear()
            for index, line in enumerate(self._vis.screen2()):
                self._display.write_text(index+1, line)
            sleep(5)

