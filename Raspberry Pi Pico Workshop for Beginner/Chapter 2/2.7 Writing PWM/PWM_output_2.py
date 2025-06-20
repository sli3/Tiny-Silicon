from machine import Pin, ADC, PWM
import time

# setting up in 26 to be ADC input
pot_pin = ADC(Pin(26))

# setting up pin 16 to be PWM output
pwm_pin = PWM(Pin(16))

# setting max constant for digital
max = 65535

# setting up constant for voltage output format MAX is 3.3V
vop = 3.3 / max


pwm_pin.freq(1000)

while True:

    # setting pot_vaule to take input from pin 26
    # .read_u16() function is to readn and take input
    pot_vaule = pot_pin.read_u16()

    # Outputing the value from the input of  pin 26 and output to pin 16
    pwm_pin.duty_u16(pot_vaule)

    # print out an input vaule from pin 26
    print(pot_vaule * vop)

    # time delay
    time.sleep(0.05)