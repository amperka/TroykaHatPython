import troykahat


# Constant for Pin 7 of Analog PI IO.
# Connect an LED to this pin.
PIN_AP_LED = 7
# Constant for Pin 3 of Analog PI IO.
# Connect an Potentiometer to this pin.
PIN_AP_POT = 3

# Gives access to all the functions of GPIO,
# that are labeled "Analog IO" on the HAT.
# See API.md for the functions reference.
ap = troykahat.analog_io()
# Configures the LED pin of Analog IO to an output mode.
ap.pinMode(PIN_AP_LED, ap.OUTPUT)
# Configures the potentiometer pin of Analog IO to an input mode.
ap.pinMode(PIN_AP_LED, ap.INPUT)

while True:

    # Read the potentiometer value
    potValue = ap.analogRead(PIN_AP_POT)
    # Set the LED brightness
    # according to potentiometer value
    ap.analogWrite(PIN_AP_LED, potValue)
