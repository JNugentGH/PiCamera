import time
import picamera

with picamera.PiCamera() as camera:
	#camera.resolution = (3280, 2464)

	camera.start_preview()

	time.sleep(2)

	camera.capture("still.jpg")
