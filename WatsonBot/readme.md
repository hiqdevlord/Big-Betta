###Automation using a Raspberry Pi 

#### Requirements

Simply install the requirements below:
- [Python 2.7 32-bit](https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi)

- [Pip](https://pip.pypa.io/en/latest/installing.html)

Use pip to install the following libraries below: 

```bash 
pip install python-twitter
pip install pyimgur
pip install picamera 
```
Note: You can use any Twitter API Wrapper for Python, I just happen to use Python-Twitter. 

####Usage

watsonCam will automatically take images using the PiCamera API.

-There are two methods located here, one for taking one picture at a time, and another for bulk images (great for creating a timelapse!). 

watsonImgur will automatically upload images using the PyImgur API.

watsonTwitter will automatically tweet a status for you. 

-For this project, we are tweeting Watson's position based on predictions made by the FishNet. Whether Watson is 'hiding' or 'swimming' will by uploaded to a .txt file. Based on Watson's status, a string from either the hiding or swimming list will be randomly selected to tweet. 

Scheduling will be done using your pi's cron file. Capture, upload and tweet as often as you desire! 

###Note
Please refer to the documentation of the following APIs and API wrappers for OAUTH help and other important details to get started. 

-[Imgur API](https://api.imgur.com/)

-[PyImgur Documentation](http://pyimgur.readthedocs.org/en/latest/reference.html)

-[Twitter API](https://dev.twitter.com/overview/documentation)

-[Python-Twitter Documentation](https://github.com/bear/python-twitter)

-[PiCamera Documentation](https://picamera.readthedocs.org/en/release-1.10/)

###Encouragement
The possibilites are endless. You can do it! 
