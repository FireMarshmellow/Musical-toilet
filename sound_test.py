from machine import Pin, TouchPad
import utime

# Initialize the GPIO pins
fx4 = Pin(19, Pin.OUT, Pin.PULL_UP)#
fx1 = Pin(21, Pin.OUT, Pin.PULL_UP)# Good 1
fx3 = Pin(22, Pin.OUT, Pin.PULL_UP)# Bad 1
fx2 = Pin(23, Pin.OUT, Pin.PULL_UP)# Bad 2

# Initialize all pins to high (no sound playing)
fx4.value(1)
fx1.value(1)
fx3.value(1)
fx2.value(1)

# List of pins
pins = [fx1, fx2, fx3, fx4]

def play_fx(sound):
    sound.value(0)
    utime.sleep(0.2)
    sound.value(1)

while True:
    play_fx(fx4)
    utime.sleep(20)