import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
print("DISTANCE IS IN PROGRESS)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
time.sleep(2)
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,FALSE)
while(GPIO.input(ECHO)==0):
  p_start=time.time()
while(GPIO.input(ECHO)==1)
  p_end=time.time()
p_dur=p_end-p_start
distance=(p_dur)*17150
distance=round(distance,2)
print("distance in cm is"+distance)
GPIO.cleanup()
