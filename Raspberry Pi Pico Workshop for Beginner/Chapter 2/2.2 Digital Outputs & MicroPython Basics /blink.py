from machine import Pin # Import pin from the machine library
import time # Import time library which lets us use the sleep command

led = Pin("LED", Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)

while True:  # Loop forever
    led.value(1)  # Turn the LED ON
    time.sleep(2) # Go to sleep for 2 seconds
        
    led.value(0)  # Turn the LED OFF
    time.sleep(2) # Go to sleep for 2 seconds