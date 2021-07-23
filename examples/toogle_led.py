import troykahat


# Constant for Pin 7 of Wiring PI IO.
# Connect an LED to this pin.
PIN_WP_LED = 7
# Constant for Pin 22 of Wiring PI IO.
# Connect an Button to this pin.
PIN_WP_BUTTON = 22

# Gives access to all the functions of GPIO,
# that are labeled "Wiring PI IO" on the HAT.
# Check WiringPI library API (https://github.com/WiringPi/WiringPi-Python)
# for the functions reference.
wp = troykahat.wiringpi_io()
# Configures the LED pin of Wiring PI IO to an output mode.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)
# Configures Button the pin of Wiring PI IO to an input mode.
wp.pinMode(PIN_WP_BUTTON, wp.INPUT)

while True:

    # If the button is pressed.
    if not wp.digitalRead(PIN_WP_BUTTON):
        # Sets HIGH voltage level for the LED pin of Wiring PI IO.
        wp.digitalWrite(PIN_WP_LED, True)
    # If the button is released.
    else:
        # Sets LOW voltage level for the LED pin of Wiring PI IO.
        wp.digitalWrite(PIN_WP_LED, False)
