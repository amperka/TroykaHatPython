def wiringpi_io():
    import wiringpi
    return wiringpi

def analog_io(i2c_address = 42):
    import gpio_expander
    return gpio_expander.GpioExpander(i2c_address)
