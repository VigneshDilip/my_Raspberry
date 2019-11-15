## LED_BLINKING_RASPBERRY PI_CODE


import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
      GPIO.output(11,True)   ## turns on the LED
      Time.sleep(1)     ## waits for one second
       GPIO.output(11,false)
       Time.sleep(1)      ## waits for one second
