import time
import RPi.GPIO as GPIO

ledPin = 32


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    pwm = GPIO.PWM(ledPin, 1000)
    pwm.start(100)


if  __name__ == '__main__':
    setup()
    try:
        while True:
             time.sleep(1)
    except KeyboardInterrupt:
        print("ende")
    
