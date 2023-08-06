from machine import Pin, TouchPad
import utime

# Create a TouchPad on pin 14
t = TouchPad(Pin(14))


while True:
    print(t.read())
    utime.sleep(0.5)