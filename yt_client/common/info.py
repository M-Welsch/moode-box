import psutil
from dataclasses import dataclass
from datetime import datetime


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

    def to_line(self):
        return ", ".join([str(val) for val in self.__dict__.values()])


class Info:
    def __init__(self, log_data: bool, datalogfile_location: str):
        self.static_network_info = psutil.net_if_addrs()
        self._ips: dict = self.obtain_ips()
        if log_data:
            self.datalogfile = f"hmi/yt_client/{datalogfile_location}/{self._timestamp(without_time_of_day=True)}.csv"
            self._write_line_to_data_logfile(", ".join(SysInfo.__dict__["__annotations__"].keys()))
        self.current_snapshot: SysInfo = self.snapshot()

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

    def snapshot(self, autosave: bool = True) -> SysInfo:
        self._update_sysinfo()
        if autosave:
            self.save_snapshot()
        return self.current_snapshot

    def _update_sysinfo(self):
        fclk = psutil.cpu_freq()
        if ":" in self._ips["eth0"] and ":" in self._ips["wlan0"]:
            self._ips = self.obtain_ips()
        self.current_snapshot = SysInfo(
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

    def save_snapshot(self):
        self._write_line_to_data_logfile(self.current_snapshot.to_line())

    def _write_line_to_data_logfile(self, line: str):
        with open(self.datalogfile, 'a') as f:
            f.write(line + '\n')

    @staticmethod
    def _timestamp(without_time_of_day: bool = False) -> str:
        timestamp = datetime.now()
        if without_time_of_day:
            return timestamp.strftime("%Y%m%d")
        else:
            return timestamp.strftime("%Y%m%d_%H%M%S")
