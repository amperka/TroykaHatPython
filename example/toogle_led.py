import troykahat


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7
# Constant for Pin 22 of Wiring PI IO.
# Connect an Button to this pin.
PIN_WP_BUTTON = 22

# Gives access to all the functions of GPIO, which are marked Wiring PI IO.
# See API for WiringPI (https://github.com/WiringPi/WiringPi-Python) library
# for the functions reference.
wp = troykahat.wiringpi_io()
# Configures Pin Led of Wiring PI IO as an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)
# Configures Pin Button of Wiring PI IO as an input mode.
wp.pinMode(PIN_WP_BUTTON, wp.INPUT)

while True:

    # If button is pressed.
    if (not(wp.digitalRead(PIN_WP_BUTTON))):
        # Sets HIGH voltage level for Pin Led of Wiring PI IO.
        wp.digitalWrite(PIN_WP_LED, True)
    # If button is released.
    else:
        # Sets LOW voltage level for Pin Led of Wiring PI IO.
        wp.digitalWrite(PIN_WP_LED, False)
