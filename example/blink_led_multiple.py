import troykahat
from time import sleep


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7
# Constant for Pin 7 of Analog PI IO.
# Connect an LED to this pin.
PIN_AP_LED = 7


# Gives access to all the functions of GPIO, that are labeled "Wiring PI IO" on the HAT.
# Check WiringPI library API (https://github.com/WiringPi/WiringPi-Python)
# for the functions reference.
wp = troykahat.wiringpi_io()
# Gives access to all the functions of GPIO, that are labeled "Analog IO" on the HAT.
# Check API.md for the functions reference.
ap = troykahat.analog_io()
# Configures the LED pin of Wiring PI IO to an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)
# Configures the LED pin of Analog IO to an output mode.
ap.pinMode(PIN_AP_LED, ap.OUTPUT)

while True:

    # Sets HIGH voltage level for the LED pin of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, True)
    # Sets HIGH voltage level for the LED pin of Analog IO.
    ap.digitalWrite(PIN_AP_LED, True)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for the LED pin of Wiring PI IO.
    wp.digitalWrite(PIN_WP_LED, False)
    # Sets HIGH voltage level for the LED pin of Analog IO.
    ap.digitalWrite(PIN_AP_LED, False)
    # Wait 500 ms.
    sleep(0.5)
