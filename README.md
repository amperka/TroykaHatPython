# TroykaHatPython

Raspberry Pi library for interaction with a Amperka TroykaHAT.

## Enabled I²C Interface

If you haven’t enabled I²C support in your Raspbian Linux yet, open the terminal and run the
following commands:

1. Run `sudo raspi-config`.
2. Use the down arrow to select **Interfacing Options**.
3. Arrow down to **I²C**.
4. Select **\<Yes\>** when it asks you to enable I²C.
5. Press **\<Ok\>** when it tells you that I²C is enabled.
6. Use the right arrow to select the **\<Finish\>** button.
7. Reboot your Raspberry Pi to make the I²C interface appear.

After the reboot, log in and enter the following command:

```shell
$ ls /dev/i2c*
```

The Pi should respond with:

```shell
/dev/i2c-1
```

This means that the I²C is on.

## Testing I²C Device Connection

For testing connection Troyka HAT board to Raspberry Pi, useful package I²C scanner.

Install the I²C scanner.

```shell
sudo apt-get install i2c-tools
```

Turn it on.

```shell
sudo i2cdetect -y 1
```

In response, Raspberry Pi will show the addresses of all connected I²C devices. Check if the `0x2A` address is present.

## Installation Library

Use **pip** to install the library:

```shell
pip3 install troykahat
```

## Quickstart example

```python
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
```

See full [API reference in API.md](https://github.com/amperka/TroykaHatPython/blob/main/API_en.md)
