import psutil
from dataclasses import dataclass


@dataclass
class SysInfo:
    cpu_fclk_min: float
    cpu_fclk_max: float
    cpu_fclk_cur: float
    cpu_temp: float
    cpu_load: float
    ip_wired: str
    ip_wifi: str
    memory_usage: float
    swap_usage: float


class Info:
    def __init__(self):
        self.static_network_info = psutil.net_if_addrs()
        self._ips: dict = self.obtain_ips()

    def obtain_ips(self) -> dict:
        try:
            eth0_ip = psutil.net_if_addrs()['eth0'][0].address
        except IndexError:
            eth0_ip = "??"
        try:
            wlan0_ip = psutil.net_if_addrs()['wlan0'][0].address
        except IndexError:
            wlan0_ip = "??"
        return {
            "eth0": eth0_ip,
            "wlan0": wlan0_ip
        }

    def snapshot(self) -> SysInfo:
        fclk = psutil.cpu_freq()
        if ":" in self._ips["eth0"] and ":" in self._ips["wlan0"]:
            self.obtain_ips()
        return SysInfo(
            cpu_fclk_min=fclk.min,
            cpu_fclk_max=fclk.max,
            cpu_fclk_cur=fclk.current,
            cpu_temp=psutil.sensors_temperatures()['cpu_thermal'][0].current,
            cpu_load=psutil.cpu_percent(),
            ip_wired=self._ips["eth0"],
            ip_wifi=self._ips["wlan0"],
            memory_usage=psutil.virtual_memory().percent,
            swap_usage=psutil.swap_memory().percent
        )
