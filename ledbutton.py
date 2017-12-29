from machine import Pin


def demo():
    print('demo digital I/O')
    led = Pin('P9', mode=Pin.OUT)
    button = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
    while 1:
        state = button.value()
        if state > 0:
            led.value(1)
        else:
            led.value(0)
