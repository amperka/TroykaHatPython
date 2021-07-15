import troykahat
from troykahat import State, Mode
from time import sleep

# Gives access to all the functions of GPIO, which are marked Wiring PI IO.
# See API for WiringPI (https://github.com/WiringPi/WiringPi-Python) library
# for the functions reference.
wp = troykahat.wiringpi_io()
# Gives access to all the functions of GPIO, which are marked Analog IO.
# See API.md for the functions reference.
ap = troykahat.analog_io()
# Configures Pin 7 of Wiring PI IO as an output mode.
wp.pinMode(7, Mode.OUTPUT)
# Configures Pin 7 of Analog IO as an output mode.
ap.pinMode(7, Mode.OUTPUT)

while True:
    # Sets HIGH voltage level for Pin 7 of Wiring PI IO.
    wp.digitalWrite(7, State.HIGH)
    # Sets HIGH voltage level for Pin 7 of Analog IO.
    ap.digitalWrite(7, State.HIGH)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for Pin 7 of Wiring PI IO.
    wp.digitalWrite(7, State.LOW)
    # Sets HIGH voltage level for Pin 7 of Analog IO.
    ap.digitalWrite(7, State.LOW)
    # Wait 500 ms.
    sleep(0.5)
