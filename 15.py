import RPi.GPIO as GPIO
from time import sleep
DIR=20 #DIRECTION GPIO PIN
STEP=21 #STEP GPIO PIN
CW=1 #CLOCKWISE ROTAION
CCW=0 #ANTICLOCKWISE ROTATION
SPR=48 #STEPS PER REVOLUTION

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.output(DIR,CW)

step_count=SPR
delay=0.0208
for x in range(step_count):
  GPIO.output(STEP,GPIO.HIGH)
  sleep(delay)
  GPIO.output(STEP,GPIO.LOW)
  sleep(delay)
  
  sleep(0.5)
  GPIO.output(DIR,CCW)
  for x in range(step_count):
    GPIO.output(STEP,GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)
    
    GPIO.cleanup()
  
