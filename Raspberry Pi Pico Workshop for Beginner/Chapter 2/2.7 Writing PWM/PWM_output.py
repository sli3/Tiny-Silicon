from machine import Pin, PWM

# setting up pin 16 to be PWM
pwm_pin = PWM(Pin(16))

# setting max constant for digital
max = 65535

pwm_pin.freq(1000)

while True:

    # setting PWM value by multiply factor to the max constant value
    PWM_value = int(0.7 * max)

    pwm_pin.duty_u16(PWM_value)