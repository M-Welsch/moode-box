from yt_client.device.pin_interface import PinInterface


class Fan:
    def __init__(self):
        self._pi: PinInterface = PinInterface.getInstance()

    def set_speed(self, speed: float) -> None:
        self._pi.set_fan_dutycycle(speed)
