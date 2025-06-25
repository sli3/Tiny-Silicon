from machine import Pin, ADC
import time

# setting up in 26 to be ADC input
pot = ADC(Pin(26))

# setting up constant for the converion factor from 0 - 65535 to 0 - 100 scale
conversion_factor = 100 / 65535

# setting up constant for last_volume
last_volume = 0

while True:

    # assign the current_volume that take reading from physical sensor
    # then multiply to conversion_factor the to make current_volume into 0 - 100 scale
    current_volume = int(pot.read_u16() * conversion_factor)
    
    # This line is to make sure that when reading the data from the sensor
    # the program will OINLY take data if the difference is MORE or LESS than 2 
    # otherwise it will DISCARD
    if ((current_volume - last_volume) >= 2 ) or ((current_volume - last_volume <= -2)):
        
        # Convert current_volume from 0 - 100 to 0 -10 scale then assign to num_bar
        num_bar = int(current_volume / 10)

        # This will do 3 things
        # 1. It will print | with the same number of num_bar value  the calculation is done by ( | * num_bar)
        # 2. It will print _ for the less of the space, the calculation is done by (10 - num_bar)
        # 3. It will print num_bar value
        print("|" * num_bar + "_" * (10 - num_bar), current_volume)
        
        # assign current_volume into last_volume
        last_volume = current_volume
    
    # time delay
    time.sleep(0.1)