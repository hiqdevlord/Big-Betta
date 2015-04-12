import pyimgur
import datetime

"""
  Upload images to Imgur automatically. 
"""

#Your keys here
CLIENT_ID = ""
CLIENT_SECRET = ""   
ACCESS_TOKEN = ""
REFRESH_TOKEN = ""

im = pyimgur.Imgur(
		CLIENT_ID, 
		CLIENT_SECRET, 
		ACCESS_TOKEN, 
		REFRESH_TOKEN
) 

im.refresh_access_token()

#makes the title the date the image was uploaded
timestamp = datetime.datetime.now()
imgpath = "image's path"
title = timestamp
#album id found imgur.com/a/'YOUR ALBUM ID'
imgalbum = im.get_album("albumid")

def watsonImgur(): 
	watson_pics = im.upload_image(path = imgpath, title= timestamp, album= imgalbum)
