import time
from w1thermsensor import W1ThermSensor
sensor=W1ThermSensor()

while True:
   temp=sensor.get_temperature()
   print("The temp is ",+temp)
   time.sleep(2)
