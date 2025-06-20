# Import Atmospheric sensor library 
from PiicoDev_BME280 import *

# Import OLED display library
from PiicoDev_SSD1306 import *

# Import Unifired library
from PiicoDev_Unified import sleep_ms

# Initialise Atmospheric sensor
sensor = PiicoDev_BME280()

# Initialise OLED display
display = create_PiicoDev_SSD1306()

while True:

    # Get data from sensor and assign to variables 
    tempC, presPa, humRH = sensor.values()
    
    # For OLED, this is a requirement to fill everything with black before print anything on it.
    # Note: everything will start from location X-axis 0 and Y-axis 0
    display.fill(0)

    ## Temperature ##
    # This line will print the word Temp at location X-axis 5 and Y-axis 10
    display.text("Temp", 5, 10)
    # This line will print reading temperature value from sensor at location X-axis 50 and Y-axis 10
    display.text(str(tempC), 50, 10)

    ## Air Pressure ##
    # This line will print the word Press at location X-axis 5 and Y-axis 30
    display.text("Press", 5, 30)
    # This line will print reading Air Pressure value from sensor at location X-axis 50 and Y-axis 30
    display.text(str(presPa), 50, 30)
    
    ## Humidity ##
    # This line will print the word Humid at location X-axis 5 and Y-axis 50
    display.text("Humid", 5, 50)
    # This line will print reading Humidity value from sensor at location X-axis 50 and Y-axis 50
    display.text(str(humRH), 50, 50)
    
    # For OLED, this is to display the data
    display.show()
