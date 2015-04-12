import picamera 
import time 
import datetime

"""
  Methods for taking pictureson the Raspberry Pi using picamera 
"""

camera = picamera.PiCamera() 

"""
  Take one image at a time, great for cron scheduling
"""
def watsonCam(): 
	#resolution, fun
	camera.resolution = (1280,720)
	#start camera
	camera.start_preview()
	#allow time for camera to set up
	time.sleep(1)
	#makes ure the picture isn't upside down
	camera.vflip = True
	#create consistent images
	camera.awb_mode = 'fluorescent'
	#set up the filename and direct path to the correct folder. 
	filename = '/usr/share/nginx/www/watson/images/fish.jpg'
	#capture the image Watson.jpg
	camera.capture(filename) 
	#give me a confirmation that it captured
	print ('captured %s' % filename)
	#close the camera 
	camera.close() 

"""
	 Take a bulk amount of images
"""
#def bulkImages(): 
#	camera.resolution = (1280, 720)
#	#time.sleep(1) # Camera warm-up time
#	camera.vflip = True
#	camera.awb_mode = 'fluorescent'
#	for i, filename in enumerate(camera.capture_continuous('/usr/share/nginx/www/watson/images/Watson.jpg')):
#       	print('Captured %s' % filename)
#	        # Capture one image a minute
#	        #decrease the time.sleep argument to take more images
#	        time.sleep(1)
#	        #this conditional will stop the iterator once 60 images have been taken, this can be changed too if you want. 
#	        watsonImgur()
#		if i == 500: 
#       	    break
