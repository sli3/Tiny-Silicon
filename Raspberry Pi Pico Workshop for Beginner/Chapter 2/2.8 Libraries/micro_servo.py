from servo import Servo
import time

my_servo = Servo(pin_id=0)

while True:
    my_servo.write(0)
    time.sleep(3.0)
    my_servo.write(90)
    time.sleep(3.0)