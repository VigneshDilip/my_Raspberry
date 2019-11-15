#This program will help us record videos using raspberry pi

import picamera
from  time import sleep #Sleep is being imported from the time library to add delay in the program
camera=picamera.PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264') # Video will be saved at desktop
sleep(5)
camera.stop_recording()
camera.stop_preview()
