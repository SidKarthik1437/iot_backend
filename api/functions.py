from RPi import _GPIO as GPIO
import time
from threading import Thread
from threading import Event


class LED():

    led_pin = 13
    flag = False
    # t: Thread

    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
        GPIO.setup(self.led_pin, GPIO.OUT)   # Set pin mode as output
        # Set pin to high(+3.3V) to off the led
        GPIO.output(self.led_pin, GPIO.HIGH)

    def blinking_led(self, lol):
        print('blink')
        while True:
            print('...led on')
            GPIO.output(self.led_pin, GPIO.LOW)  # led on
            time.sleep(1)
            print('led off...')
            GPIO.output(self.led_pin, GPIO.HIGH)  # led off
            time.sleep(1)

            if lol():
                self.clean()
                print('stopping')
                break

    def clean(self):
        GPIO.output(self.led_pin, GPIO.HIGH)     # led off
        GPIO.cleanup()

    def start(self):
        self.setup()
        self.t = Thread(target=self.blinking_led, args=(lambda: self.flag, ))
        self.t.start()
        print('starting')

    def stop(self):
        self.flag = True
        self.t.join()


led = LED()
