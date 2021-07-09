import wiringpi
from pin import State, Mode

class GpioExpanderCommands():
    """
    Return 32 bit unic id stm32f030f4p6 (UID).
    """
    UID = 0x00

    """
    Reset chip.
    """
    RESET_SLAVE = 0x01

    """
    Set new I²C address on chip. Restart I²C peripheral with new slave address.
    After power off or reset, device will start with old I²C address.
    """
    CHANGE_I2C_ADDR = 0x02

    """
    Save current I2C address on flash, if it was changed by 
    «CHANGE_I2C_ADDR», or «CHANGE_I2C_ADDR_IF_UID_OK» command
    After power off or reset, device will start with new I²C address.
    """
    SAVE_I2C_ADDR = 0x03

    """
    Set input mode on virtual port 0 pins. If argument is 0b0000000000000101, 
    virtual pins 0 and 2 will be set on input mode.
    """
    PORT_MODE_INPUT = 0x04

    """
    Set input pullup mode on virtual port 0 pins. If argument is 0b0000000000000101, 
    virtual pins 0 and 2 will be set on input pullup mode.
    """
    PORT_MODE_PULLUP = 0x05

    """
    Set input pulldown mode on virtual port 0 pins. If argument is 0b0000000000000101, 
    virtual pins 0 and 2 will be set on input pulldown mode.
    """
    PORT_MODE_PULLDOWN = 0x06

    """
    Set output mode on virtual port 0 pins. If argument is 0b0000000000000101, 
    virtual pins 0 and 2 will be set on output mode with low value.
    """
    PORT_MODE_OUTPUT = 0x07

    """
    Return digital value of virtual port 0. Answer 0b0000000000000101 means virtual pins 0 and 2 is high, 
    and all other pins is low. Not change pin mode.
    """
    DIGITAL_READ = 0x08

    """
    Set high digital value of virtual port 0 with change pin mode to output. 
    If argument is 0b0000000000000101, virtual pins 0 and 2 will be output with high value.
    All other pins value is not change. Change pin mode to output.
    """
    DIGITAL_WRITE_HIGH = 0x09

    """
    Set low digital value of virtual port 0 with change pin mode to output. If argument is 0b0000000000000101, 
    virtual pins 0 and 2 will be output with low value.
    All other pins value is not change. Change pin mode to output.
    """
    DIGITAL_WRITE_LOW = 0x0A

    """
    Writes an analog value (PWM wave) to a pin. The pin will generate a steady square wave of the specified duty cycle.
    Default frequency of the PWM signal 1 kHz. Change pin mode to output.
    """
    ANALOG_WRITE = 0x0B

    """
    Return analog values of pin (TODO - adc max value). ADC conversion is never stop,
    so value can be readed immediately. Not change pin mode.
    """
    ANALOG_READ = 0x0C

    """
    Set the PWM frequency on all pins at the same time. The PWM filling factor does not change.
    """
    PWM_FREQ = 0x0D

    """
    Set ADC conversion speed. Value must be in range from 0 to 7.
    0: Sampling time 1.5 ADC clock cycle
    1: Sampling time 7.5 ADC clock cycles
    2: Sampling time 13.5 ADC clock cycles
    3: Sampling time 28.5 ADC clock cycles
    4: Sampling time 41.5 ADC clock cycles
    5: Sampling time 55.5 ADC clock cycles
    6: Sampling time 71.5 ADC clock cycles
    7: Sampling time 239.5 ADC clock cycles
    """
    ADC_SPEED = 0x0E

    """
    When many I²C devices have the same I²C address, I²C master can read UID of devices 
    with this address (UID command). Only one device can send correct UID.
    To set new addres on that device, I²C master must send readed UID to I²C slaves with command «MASTER_READED_UID». 
    If UID is belongs to slave, that slave device can change i²c address with the command «CHANGE_I2C_ADDR_IF_UID_OK».
    """
    MASTER_READED_UID = 0x0F

    """
    Set new I²C address on slave device, if slave recieve his UID on «MASTER_READED_UID» command
    """
    CHANGE_I2C_ADDR_IF_UID_OK = 0x10

    """
    Command to identify of I2Cadio device on I2C address. If slave answer is «slot», 
    then we can addressing it with UID, see «MASTER_READED_UID».
    """
    SAY_SLOT = 0x11

    """
    Turning on ADC low pass filter.
    """
    ADC_LOWPASS_FILTER_ON = 0x20

    """
    Turning of ADC low pass filter.
    """
    ADC_LOWPASS_FILTER_OFF = 0x21

    """
    Set treshold for «ADC_AS_DIGITAL_PORT_READ».
    """
    ADC_AS_DIGITAL_PORT_SET_TRESHOLD = 0x22

    """
    Return digital value of virtual port 0 from pins analog value. 
    Answer 0b0000000000000101 means analog value on virtual pins 0 and 2 is equal or larger than treshold.
    Not change pin mode.
    """
    ADC_AS_DIGITAL_PORT_READ = 0x23


commands = GpioExpanderCommands

class GpioExpander(object):

    def __init__(self, i2c_address):
        wiringpi.wiringPiSetup()
        self._i2c = wiringpi.I2C()
        self._io = self._i2c.setupInterface('/dev/i2c-1', i2c_address)

    def pinMode(self, pin, mode):
        data = self._reverse_uint16(0x0001 << pin)
        if (mode == Mode.INPUT):
            self._i2c.writeReg16(
                self._io, commands.PORT_MODE_INPUT, data)
        elif (mode == Mode.INPUT_PULLUP):
            self._i2c.writeReg16(
                self._io, commands.PORT_MODE_PULLUP, data)
        elif (mode == Mode.INPUT_PULLDOWN):
            self._i2c.writeReg16(
                self._io, commands.PORT_MODE_PULLDOWN, data)
        elif (mode == Mode.OUTPUT):
            self._i2c.writeReg16(
                self._io, commands.PORT_MODE_OUTPUT, data)

    def digitalRead(self, pin):
        mask = 0x0001 << pin
        result = 0
        if self._digitalReadPort() & mask:
            result = 1
        return result

    def digitalWrite(self, pin, value):
        data = self._reverse_uint16(0x0001 << pin)
        if value:
            self._i2c.writeReg16(
                self._io, commands.DIGITAL_WRITE_HIGH, data)
        else:
            self._i2c.writeReg16(
                self._io, commands.DIGITAL_WRITE_LOW, data)

    def analogRead(self, pin):
        return self._analogRead16(pin)/4095.0

    def analogWrite(self, pin, value):
        value = int(value*255)
        data = (pin & 0xff) | ((value & 0xff) << 8)
        self._i2c.writeReg16(self._io, commands.ANALOG_WRITE, data)

    def reset(self):
        self._i2c.write(self._io, commands.RESET)

    def changeAddress(self, newAddress):
        self._i2c.writeReg16(self._io, commands.CHANGE_I2C_ADDR, newAddress)

    def saveAddress(self):
        self._i2c.write(self._io, commands.SAVE_I2C_ADDR)

    def _reverse_uint16(self, data):
        result = ((data & 0xff) << 8) | ((data >> 8) & 0xff)
        return result

    def _digitalReadPort(self):
        port = self._reverse_uint16(self._i2c.readReg16(
            self._io, commands.DIGITAL_READ))
        return port

    def _digitalWritePort(self, value):
        value = self._reverse_uint16(value)
        self._i2c.writeReg16(self._io, commands.DIGITAL_WRITE_HIGH, value)
        self._i2c.writeReg16(self._io, commands.DIGITAL_WRITE_LOW, ~value)

    def _analogRead16(self, pin):
        self._i2c.writeReg16(self._io, commands.ANALOG_READ, pin)
        return self._reverse_uint16(self._i2c.readReg16(self._io, commands.ANALOG_READ))

    def _setPwmFreq(self, freq):
        self._i2c.writeReg16(
            self._io, commands.PWM_FREQ, self._reverse_uint16(freq))
