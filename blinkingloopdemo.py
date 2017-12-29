# from machine import Pin
import time


led = Pin('P9', mode=Pin.OUT)


def demo():
    while True:
        led.value(0)
        time.sleep(2)
        led.value(1)
        time.sleep(2)
