def wiringpi_io():
    """Creates and returns the reference to the wiringpi module for work
    with pins are marked as "Wiring Pi IO" on the Troyka HAT board.

    Returns:
    --------
    Object wiringpi. See API for WiringPI (https://github.com/WiringPi/WiringPi-Python) 
    library for the functions reference.
    """
    import wiringpi
    wiringpi.wiringPiSetup()
    return wiringpi


def analog_io(i2c_address=42):
    """Creates and returns the new analog_io object to work
    with pins marked as "Analog IO" on the Troyka HAT board.

    Optional parameters:
    -------------------
    i2c_address: int
        Device address on the I²C bus. When called without a parameter,
        the default address is 42.

    Returns:
    --------
    Object gpio_expander. See API.md for the functions reference.
    """
    from troykahat import gpio_expander
    return gpio_expander.GpioExpander(i2c_address)
