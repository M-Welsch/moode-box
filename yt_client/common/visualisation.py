from typing import List

from yt_client.common import Info
from yt_client.common.info import SysInfo


class Visualisation:
    def __init__(self, info: Info):
        self._info = info
        self._snapshot: SysInfo

    def update_sysinfo(self):
        self._snapshot = self._info.snapshot()

    def screen1(self) -> List[str]:
        fclk_percent = self._snapshot.cpu_fclk_cur / self._snapshot.cpu_fclk_max*100
        return [
            f"CPU Load: {self._snapshot.cpu_load} %",
            f"CPU Temp: {self._snapshot.cpu_temp} °C",
            f"CPU Clk: {self._snapshot.cpu_fclk_cur} MHz",
            f"{fclk_percent:.1f} % von clkmax",
            f"Mem usage: {self._snapshot.memory_usage} %"
        ]

    def screen2(self) -> List[str]:
        return [
            f"IP LAN:",
            f"{self._snapshot.ip_wired}",
            "",
            f"IP WIFI:",
            f"{self._snapshot.ip_wifi}"
        ]
