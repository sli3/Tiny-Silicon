from machine import  Pin
import time

# set up pin 15 as an input to read our button's state
button = Pin(15, Pin.IN)

# setup pin 16 as an output for LED
led = Pin(16, Pin.OUT)

while True:
    time.sleep(.2)
    
    if button.value() == 1:
        timer = timer + 1
    print(timer)