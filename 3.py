## RASPBERRY_PI_ CODE_FOR_BUZZER

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
buzzer=23
GPIO.setup(buzzer,OUTPUT)
while TRUE:
   GPIO.output(buzzer,HIGH)
    print(“BEEP”)
    sleep(2) ##for 2 seconds
    GPIO.output(buzzer,LOW)
    sleep(1)
