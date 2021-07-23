import wiringpi


class GpioExpander(object):
    """Gives access to the control methods of the pins connected to 
     the I²C expander based on the STM32F030F4P6 controller.
    In the case of Troyka HAT, these are the pins labeled as "Analog IO"
    on the Troyka HAT board. To create an object, use the "analog_io" function.
    """

    UID = 0x00
    """Return 32 bit unic id stm32f030f4p6 (UID).
    """

    RESET = 0x01
    """Reset chip.
    """

    CHANGE_I2C_ADDR = 0x02
    """Set new I²C address on chip. Restart I²C peripheral with new slave address.
    After power off or reset, device will start with old I²C address.
    """

    SAVE_I2C_ADDR = 0x03
    """Save current I2C address on flash, if it was changed by
    «CHANGE_I2C_ADDR», or «CHANGE_I2C_ADDR_IF_UID_OK» command
    After power off or reset, device will start with new I²C address.
    """

    INPUT = 0x04
    """Set input mode on virtual port 0 pins. If argument is
    0b0000000000000101, virtual pins 0 and 2 will be set on input mode.
    """

    INPUT_PULLUP = 0x05
    """Set input pullup mode on virtual port 0 pins. If argument is
    0b0000000000000101, virtual pins 0 and 2 will be set on input pullup mode.
    """

    INPUT_PULLDOWN = 0x06
    """Set input pulldown mode on virtual port 0 pins.
    If argument is 0b0000000000000101,
    virtual pins 0 and 2 will be set on input pulldown mode.
    """

    OUTPUT = 0x07
    """Set output mode on virtual port 0 pins.
    If argument is 0b0000000000000101,
    virtual pins 0 and 2 will be set on output mode with low value.
    """

    DIGITAL_READ = 0x08
    """Return digital value of virtual port 0.
    Answer 0b0000000000000101 means virtual pins 0 and 2 is high,
    and all other pins is low. Not change pin mode.
    """

    DIGITAL_WRITE_HIGH = 0x09
    """Set high digital value of virtual port 0 with change pin mode to output.
    If argument is 0b0000000000000101,
    virtual pins 0 and 2 will be output with high value.
    All other pins value is not change. Change pin mode to output.
    """

    DIGITAL_WRITE_LOW = 0x0A
    """Set low digital value of virtual port 0 with change pin mode to output.
    If argument is 0b0000000000000101,
    virtual pins 0 and 2 will be output with low value.
    All other pins value is not change. Change pin mode to output.
    """

    ANALOG_WRITE = 0x0B
    """Writes an analog value (PWM wave) to a pin.
    The pin will generate a steady square wave of the specified duty cycle.
    Default frequency of the PWM signal 1 kHz. Change pin mode to output.
    """

    ANALOG_READ = 0x0C
    """Return analog values of pin (TODO - adc max value).
    ADC conversion is never stop,
    so value can be readed immediately. Not change pin mode.
    """

    PWM_FREQ = 0x0D
    """Set the PWM frequency on all pins at the same time.
    The PWM filling factor does not change.
    """

    ADC_SPEED = 0x0E
    """Set ADC conversion speed. Value must be in range from 0 to 7.
    0: Sampling time 1.5 ADC clock cycle
    1: Sampling time 7.5 ADC clock cycles
    2: Sampling time 13.5 ADC clock cycles
    3: Sampling time 28.5 ADC clock cycles
    4: Sampling time 41.5 ADC clock cycles
    5: Sampling time 55.5 ADC clock cycles
    6: Sampling time 71.5 ADC clock cycles
    7: Sampling time 239.5 ADC clock cycles
    """

    MASTER_READED_UID = 0x0F
    """When many I²C devices have the same I²C address,
    I²C master can read UID of devices with this address (UID command).
    Only one device can send correct UID.
    To set new addres on that device, I²C master must send read UID to
    I²C slaves with command «MASTER_READED_UID».
    If UID is belongs to slave, that slave device can change i²c address
    with the command «CHANGE_I2C_ADDR_IF_UID_OK».
    """

    CHANGE_I2C_ADDR_IF_UID_OK = 0x10
    """Set new I²C address on slave device,
    if slave receive his UID on «MASTER_READED_UID» command
    """

    SAY_SLOT = 0x11
    """Command to identify of I²C device on I²C address.
    If slave answer is «slot», then we can addressing it with UID,
    see «MASTER_READED_UID».
    """

    ADC_LOWPASS_FILTER_ON = 0x20
    """Turning on ADC low pass filter.
    """

    ADC_LOWPASS_FILTER_OFF = 0x21
    """Turning of ADC low pass filter.
    """

    ADC_AS_DIGITAL_PORT_SET_TRESHOLD = 0x22
    """Set treshold for «ADC_AS_DIGITAL_PORT_READ».
    """

    ADC_AS_DIGITAL_PORT_READ = 0x23
    """Return digital value of virtual port 0 from pins analog value.
    Answer 0b0000000000000101 means analog value on virtual pins 0 and 2
    is equal or larger than treshold. Not change pin mode.
    """

    def __init__(self, i2c_address):
        """The constructor for GpioExpander class.

        Optional parameters:
        --------------------
        i2c_address: int
            Device address on the I²C bus. When called without a parameter,
            the default address is 42.
        """
        wiringpi.wiringPiSetup()
        self._i2c = wiringpi.I2C()
        self._io = self._i2c.setupInterface("/dev/i2c-1", i2c_address)

    def pinMode(self, pin, mode):
        """Configures the pin mode.

        Parameters:
        -----------
        pin: int
            The number of the pin indexed from `0` to `7`
            with an index from 0 to 7 on the group "Analog IO".
        mode: pin mode:
            INPUT: input mode.
            INPUT_PULLUP: pull-up input mode.
            INPUT_PULLDOWN: pull-down input mode.
            OUTPUT: output mode.

        Returns:
        --------
        None
        """

        data = self._reverse_uint16(1 << pin)
        self._i2c.writeReg16(self._io, mode, data)

    def digitalRead(self, pin):
        """Reads the digital value from a pin.

        Parameters:
        -----------
        pin: int
            The number of the pin indexed from `0` to `7`
            with an index from 0 to 7 on the group "Analog IO".

        Returns:
        --------
        True: High level of 3.3 V.
        False: Low level of 0 V.

        """
        mask = 1 << pin
        result = 0
        if self._digitalReadPort() & mask:
            result = 1
        return result

    def digitalWrite(self, pin, value):
        """
        Sets the digital value to a pin.

        Parameters:
        -----------
        pin: int
            The number of the pin indexed from `0` to `7`
            with an index from 0 to 7 on the group "Analog IO".
        value: bool
            True / 1 — corresponds to the high level of 3.3 V.
            False / 0 — corresponds to the low level of 0 V.

        Returns:
        --------
        None
        """
        data = self._reverse_uint16(1 << pin)
        state = (
            GpioExpander.DIGITAL_WRITE_HIGH if value else GpioExpander.DIGITAL_WRITE_LOW
        )
        self._i2c.writeReg16(self._io, state, data)

    def analogRead(self, pin):
        """Reads the analog value from a pin.

        Parameters:
        -----------
        pin: int
            The number of the pin indexed from `0` to `7`
            with an index from 0 to 7 on the group "Analog IO".

        Returns:
        --------
        Returns a value from 0.0 to 1.0, directly corresponding to
        a pin voltage from 0 V to 3.3 V.
        """
        return self._analogRead16(pin) / 4095.0

    def analogWrite(self, pin, value):
        """Sets the analog value to a pin.

        Parameters:
        -----------
        pin: int
            The number of the pin indexed from `0` to `7`
            with an index from 0 to 7 on the group "Analog IO".
        value: float
            The value from 0.0 to 1.0, directly corresponding to
            PWM duty cycle from 0 to 100%.

        Returns:
        --------
        None
        """
        value = int(value * 255)
        data = (pin & 0xFF) | ((value & 0xFF) << 8)
        self._i2c.writeReg16(self._io, GpioExpander.ANALOG_WRITE, data)

    def changeAddress(self, newAddress):
        """
        Changes the I²C address of the board.

        Parameters:
        -----------
        newAddress: int
            New I²C address of the board.

        Returns:
        --------
        None
        """
        self._i2c.writeReg16(
            self._io, GpioExpander.CHANGE_I2C_ADDR, newAddress)

    def saveAddress(self):
        """
        Saves the current I²C address of the board to the EEPROM,
        which was previously changed using the "changeAddress" method.

        Returns:
        --------
        None
        """
        self._i2c.write(self._io, GpioExpander.SAVE_I2C_ADDR)

    def _reset(self):
        self._i2c.write(self._io, GpioExpander.RESET)

    def _reverse_uint16(self, data):
        result = ((data & 0xFF) << 8) | ((data >> 8) & 0xFF)
        return result

    def _digitalReadPort(self):
        port = self._reverse_uint16(
            self._i2c.readReg16(self._io, GpioExpander.DIGITAL_READ)
        )
        return port

    def _digitalWritePort(self, value):
        value = self._reverse_uint16(value)
        self._i2c.writeReg16(self._io, GpioExpander.DIGITAL_WRITE_HIGH, value)
        self._i2c.writeReg16(self._io, GpioExpander.DIGITAL_WRITE_LOW, ~value)

    def _analogRead16(self, pin):
        self._i2c.writeReg16(self._io, GpioExpander.ANALOG_READ, pin)
        return self._reverse_uint16(self._i2c.readReg16(
                                    self._io, GpioExpander.ANALOG_READ))

    def _setPwmFreq(self, freq):
        self._i2c.writeReg16(self._io, GpioExpander.PWM_FREQ,
                             self._reverse_uint16(freq))
