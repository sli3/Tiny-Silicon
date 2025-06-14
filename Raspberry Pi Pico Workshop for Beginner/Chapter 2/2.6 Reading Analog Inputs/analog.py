from machine import Pin, ADC
import time

# setup pin 26 as analog input
pot = ADC(Pin(26))

# constant to convert the - - 65535 range to 0 - 3.3 volts
conversion_factor = 3.3 / 65535

while True:
    # read analog input vand store it in a variable call pot_voltage
    pot_voltage = pot.read_u16() * conversion_factor

    # print pot_voltage
    print(pot_voltage)
    time.sleep(0.1)