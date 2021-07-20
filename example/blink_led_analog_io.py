import troykahat
from time import sleep


# Constant for Pin 7 of Analog PI IO.
# Connect an LED to this pin.
PIN_AP_LED = 7


# Gives access to all the functions of GPIO, which are marked Analog IO.
# See API.md for the functions reference.
ap = troykahat.analog_io()
# Configures Pin Led of Analog IO as an output mode.
ap.pinMode(PIN_AP_LED, ap.OUTPUT)

while True:

    # Sets HIGH voltage level for Pin Led of Analog IO.
    ap.digitalWrite(PIN_AP_LED, True)
    # Wait 500 ms.
    sleep(0.5)
    # Sets HIGH voltage level for Pin Led of Analog IO.
    ap.digitalWrite(PIN_AP_LED, False)
    # Wait 500 ms.
    sleep(0.5)
