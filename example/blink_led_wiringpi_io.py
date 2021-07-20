import troykahat
from time import sleep


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7


# Gives access to all the functions of GPIO, which are marked Wiring PI IO.
# See API for WiringPI (https://github.com/WiringPi/WiringPi-Python) library
# for the functions reference.
wp = troykahat.wiringpi_io()
# Configures Pin Led of Wiring PI IO as an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)

while True:

    # Sets HIGH voltage level for Pin Led of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, True)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for Pin Led of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, False)
    # Wait 500 ms.
    sleep(0.5)
