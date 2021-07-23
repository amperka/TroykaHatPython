import troykahat
from time import sleep


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7


# Gives access to all the functions of GPIO, that are labeled "Wiring PI IO" on the HAT.
# Check WiringPI library API (https://github.com/WiringPi/WiringPi-Python)
# for the functions reference.
wp = troykahat.wiringpi_io()
# Configures the LED pin of Wiring PI IO to an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)

while True:

    # Sets HIGH voltage level for the LED pin of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, True)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for the LED pin of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, False)
    # Wait 500 ms.
    sleep(0.5)
