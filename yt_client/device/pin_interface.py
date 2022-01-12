from yt_client.device.utils import hardware


if hardware() == "rpi":
    import RPi.GPIO as GPIO
else:
    from mockup import GPIO


class Pins:
    fan = 12  # GPIO 12 (BOARD) or pin 32 (BCM)


class PinInterface:
    __instance = None

    @staticmethod
    def getInstance():
        if PinInterface.__instance is None:
            PinInterface()
        return PinInterface.__instance

    def __init__(self):
        if PinInterface.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PinInterface.__instance = self
        # GPIO.cleanup()
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Pins.fan, GPIO.OUT)
        GPIO.output(Pins.fan, GPIO.LOW)
        self.fan_pwm = GPIO.PWM(Pins.fan, 50)
        self.fan_pwm .start(100)

    def set_fan_dutycycle(self, dc: float):
        dc = limit(dc, 0, 100)
        self.fan_pwm.ChangeDutyCycle(dc)

    def set_fan_pwm_frequency(self, freq_hz: float):
        self.fan_pwm.ChangeFrequency(freq_hz)

    def teardown(self):
        GPIO.cleanup()


def limit(num, minimum: float, maximum: float) -> float:
    return max(min(num, maximum), minimum)
