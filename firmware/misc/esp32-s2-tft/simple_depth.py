
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A1)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def get_depth(pin):
    return (pin.value * 3.3) / 65536 * 1000  / 3.2 / 2.54 # inches


while True:
    #print((get_voltage(analog_in),"volts"))
    print(get_depth(analog_in), "cm")
    time.sleep(.5)
