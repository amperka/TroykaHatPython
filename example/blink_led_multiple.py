import troykahat
from time import sleep


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7
# Constant for Pin 7 of Analog PI IO.
# Connect an LED to this pin.
PIN_AP_LED = 7


# Gives access to all the functions of GPIO, which are marked Wiring PI IO.
# See API for WiringPI (https://github.com/WiringPi/WiringPi-Python) library
# for the functions reference.
wp = troykahat.wiringpi_io()
# Gives access to all the functions of GPIO, which are marked Analog IO.
# See API.md for the functions reference.
ap = troykahat.analog_io()
# Configures Pin Led of Wiring PI IO as an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)
# Configures Pin Led of Analog IO as an output mode.
ap.pinMode(PIN_AP_LED, ap.OUTPUT)

while True:

    # Sets HIGH voltage level for Pin Led of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, True)
    # Sets HIGH voltage level for Pin Led of Analog IO.
    ap.digitalWrite(PIN_AP_LED, True)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for Pin Led of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, False)
    # Sets HIGH voltage level for Pin Led of Analog IO.
    ap.digitalWrite(PIN_AP_LED, False)
    # Wait 500 ms.
    sleep(0.5)
