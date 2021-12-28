from time import sleep
import logging

from yt_client.common import Info
from yt_client.common.visualisation import Visualisation
from yt_client.device import Display, Fan

LOG = logging.getLogger(__name__)


class Loop:
    def __init__(self, loop_cfg: dict, info: Info):
        self._info = info
        self._display = Display()
        self._fan = Fan()
        self._vis = Visualisation(self._info)
        self._cfg = loop_cfg

    def start(self):
        while True:
            self._fan.set_speed(100)
            self._display.clear()
            self._vis.update_sysinfo()
            for index, line in enumerate(self._vis.screen1()):
                self._display.write_text(index+1, line)
            sleep(self._cfg['screen_switch_interval_s'])
            self._display.clear()
            for index, line in enumerate(self._vis.screen2()):
                self._display.write_text(index+1, line)
            sleep(self._cfg['screen_switch_interval_s'])
