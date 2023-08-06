from machine import Pin, TouchPad
import utime

# Initialize the GPIO pins
fx4 = Pin(19, Pin.OUT, Pin.PULL_UP)
fx1 = Pin(21, Pin.OUT, Pin.PULL_UP)
fx3 = Pin(22, Pin.OUT, Pin.PULL_UP)
fx2 = Pin(23, Pin.OUT, Pin.PULL_UP)

# Initialize all pins to high (no sound playing)
fx4.value(1)
fx1.value(1)
fx3.value(1)
fx2.value(1)

# Create a TouchPad on pin 14
t = TouchPad(Pin(14))

touch_start_time = None
sound_effect_1_playing = False
sound_effect_3_played = False
sound_effect_4_played = False

while True:
    # Read the touch sensor
    value = t.read()

    if value < 110:  # Touch detected
        if touch_start_time is None:  # Start of the touch
            touch_start_time = utime.time()
            print("Touch detected!")

            # Start playing sound effect 1 (if it's not already playing)
            if not sound_effect_1_playing:
                fx1.value(0)  # Start the sound by bringing the pin low
                utime.sleep(0.5)  # Let the pin stay low for a moment
                fx1.value(1)  # Bring the pin back to high

                sound_effect_1_playing = True

    else:  # No touch detected
        # If sound effect 1 was playing, stop it and play sound effect 2
        if sound_effect_1_playing:
            fx1.value(0)  # Stop sound effect 1 by bringing the pin low
            utime.sleep(0.5)  # Let the pin stay low for a moment
            fx1.value(1)  # Bring the pin back to high

            fx2.value(0)  # Start sound effect 2
            utime.sleep(0.5)  # Let sound effect 2 play for a moment
            fx2.value(1)  # Stop sound effect 2

            sound_effect_1_playing = False

        # Reset the touch timer
        touch_start_time = None
        sound_effect_3_played = False
        sound_effect_4_played = False

    # If the touch has lasted more than 10 minutes, play sound effect 3
    if touch_start_time is not None:
        if utime.time() - touch_start_time >= 15 and not sound_effect_3_played:
            print("Touch detected for more than 10 minutes!")

            fx1.value(0)  # Stop sound effect 1 by bringing the pin low
            utime.sleep(0.5)  # Let the pin stay low for a moment
            fx1.value(1)  # Bring the pin back to high

            fx3.value(0)  # Start sound effect 3
            utime.sleep(0.5)  # Let sound effect 3 play for a moment
            fx3.value(1)  # Stop sound effect 3

            sound_effect_1_playing = False
            sound_effect_3_played = True

            # Start playing sound effect 1 (if it's not already playing)
            if not sound_effect_1_playing:
                fx1.value(0)  # Start the sound by bringing the pin low
                utime.sleep(0.5)  # Let the pin stay low for a moment
                fx1.value(1)  # Bring the pin back to high

                sound_effect_1_playing = True

        # If the touch has lasted more than 15 minutes, play sound effect 4
        if utime.time() - touch_start_time >= 20 and not sound_effect_4_played:
            print("Touch detected for more than 15 minutes!")

            fx4.value(0)  # Start sound effect 4
            utime.sleep(0.5)  # Let sound effect 4 play for a moment
            fx4.value(1)  # Stop sound effect 4

            sound_effect_1_playing = False
            sound_effect_4_played = True

    # Delay for a second
    utime.sleep(1)

