# TroykaHatPython API (EN)

## `wiringpi_io() -> wiringpi`

Creates and returns the reference to the `wiringpi` module for work with pins labeled as "Wiring Pi IO" on the Troyka HAT board. These pins are connected directly to Raspberry Pi via GPIO connector.

_Check the [WiringPi library documentation](https://pypi.org/project/wiringpi/) for details._

## `analog_io(i2c_address: int=42) -> GpioExpander`

Creates and returns the new `analog_io` object to work with pins labeled as "Analog IO" on the Troyka HAT board. These pins are connected to the I²C expander based on STM32F030F4P6 controller.

_Use the `GpioExpander` class methods for communication._

- `i2c_address`: the I²C bus address of the device. When omitted, uses default address — decimal `42`.

## `class GpioExpander`

Gives access to the control methods of the pins connected to the I²C expander based on the STM32F030F4P6 controller. In the case of Troyka HAT, these are the pins labeled as "Analog IO" on the Troyka HAT board. To create an object, use the `analog_io` function.

### `pinMode(pin: int, mode: int) -> None`

Configures the pin mode.

- `pin`:  the number of the pin indexed from `0` to `7` on the "Analog IO" group of Troyka HAT board.
- `mode`: pin mode:
  - `INPUT`: input mode.
  - `INPUT_PULLUP`: pull-up input mode.
  - `INPUT_PULLDOWN`: pull-down input mode.
  - `OUTPUT`: output mode.

### `digitalRead(pin: int) -> bool`

Reads the digital value from a pin.

- `pin`: the number of the pin indexed from `0` to `7` on the "Analog IO" group of Troyka HAT board.

Value returned:

- `True` — high level of 3.3 V.
- `False` — low level of 0 V.

The pin has to be configured to the input mode with `pinMode` method first.

### `digitalWrite(pin: int, value: bool) -> None`

Sets the digital value to a pin.

- `pin`:  the number of the pin indexed from `0` to `7` on the "Analog IO" group of Troyka HAT board.
- `value`: 
    - `True / 1` — corresponds to the high level of 3.3 V.
    - `False / 0` — corresponds to the low level of 0 V.

The pin has to be configured to the output mode with `pinMode` method first.

### `analogRead(pin: int) -> float`

Reads the analog value from a pin.

- `pin`:  the number of the pin indexed from `0` to `7` on the "Analog IO" group of Troyka HAT board.

Returns a value from `0.0` to `1.0`, directly corresponding to a pin voltage from 0 V to 3.3 V.

The pin has to be configured to the input mode with `pinMode` method first.

### `analogWrite(pin: int, value: float) -> None`

Sets the analog value to a pin.

- `pin`:  the number of the pin indexed from `0` to `7` on the "Analog IO" group of Troyka HAT board.
- `value`: the value from `0.0` to `1.0`, directly corresponding to the PWM duty cycle from 0 to 100%.

The pin has to be configured to the output mode with `pinMode` method first.

### `changeAddress(newAddress: int) -> None`

Changes the I²C address of the board.

- `newAddress`: new I²C address of the board.

When the power of Troyka HAT is turned off, the address is set to the default `42`. If you want to change the address constantly, change it and then use the `saveAddress` method to save it.

### `saveAddress() -> None`

Saves the current I²C address of the board to the EEPROM, which was previously changed using the `changeAddress` method.
