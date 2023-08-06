from machine import Pin, TouchPad
import random
import utime
import machine

# Initialize the GPIO pins
fx1 = Pin(21, Pin.OUT, Pin.PULL_UP)# Good 1 9S
fx2 = Pin(22, Pin.OUT, Pin.PULL_UP)# Bad 2 11S
fx3 = Pin(23, Pin.OUT, Pin.PULL_UP)# Bad 1 11S
fx4 = Pin(19, Pin.OUT, Pin.PULL_UP)# Good 2 9S


fx1.value(1)
fx2.value(1)
fx3.value(1)
fx4.value(1)

# Initialize the IR sensor and touch sensor
ir_sensor = Pin(5, Pin.IN, Pin.PULL_DOWN)
# Create a TouchPad on pin 14
t = TouchPad(Pin(14))

choice = None

def play_fx(sound):
    sound.value(0)
    utime.sleep(0.2)
    sound.value(1)

def ir_sensor_handler(choice):    
    choice = random.choice([1, 2])
    if choice == 1:
        play_fx(fx1)
        utime.sleep(10)
        print('YES DO IT YES')
        for i in range(20):
            if t.read() < 300:
                play_fx(fx4)
                print('OH YES THANK YOU. YASSSS')
                utime.sleep(1)
                machine.reset()
            else:
                pass
        machine.reset()
                
            
    elif choice == 2:
        play_fx(fx2)
        utime.sleep(12)
        print('NO PLEeas NOO')
        for i in range(20):
            if t.read() < 300:
                play_fx(fx3)
                print('AHHH WHY GOD WHY ME!')
                utime.sleep(1)
                machine.reset()
            else:
                pass
        machine.reset()


while True:
    print(ir_sensor.value())
    print(t.read())
    if ir_sensor.value() == 0:
        ir_sensor_handler(choice)
    utime.sleep(1)  # Sleep for 1 second