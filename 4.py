##THIS CODE IS TO TAKE 5 PICTURES IN A ROW
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
