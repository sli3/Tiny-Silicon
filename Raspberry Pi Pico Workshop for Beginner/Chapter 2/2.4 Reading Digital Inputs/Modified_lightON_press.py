from machine import Pin
import time

button = Pin(15, Pin.IN)
led = Pin(16, Pin.OUT)

last_button_state = -1

while True:
    current_button_state = button.value()
    
    if current_button_state != last_button_state:
        if current_button_state == 1:
            print("Button Pressed!")
            led.value(1)
        else:
            print("Button Released!")
            led.value(0)
            
        last_button_state = current_button_state
        
    time.sleep(0.05)