from machine import Pin
import time

### ORIGINAL CODE USE FOR PICO 1 ###
# set up pin 15 as an input with a pull-down resistor
#button = Pin(15, Pin.IN, Pin.PULL_DOWN)

### MODIFIED CODE USE FOR PICO 2 ###
button = Pin(15, Pin.IN)

# set up pin 16 connected to the LED as an output
led = Pin(16, Pin.OUT)

while True:
    # if the button is pressed, then turn on the LED
    if button.value() == 1:
        led.value(1)
    
    # if its not pressed, then turn the LED off
    else:
        led.value(0)

