from .troykahat import wiringpi_io, analog_io

class State():
    LOW = 0
    HIGH = 1


class Mode():
    INPUT = 0
    OUTPUT = 1
    INPUT_PULLUP = 2
    INPUT_PULLDOWN = 3
