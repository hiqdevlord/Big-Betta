### How to Train your <s>Dragon</s> <s>Betta Fish</s> Neural Network

This script is made for training the FishNet. We wrote it to work with any given image size.
It also outputs to a ``.csv`` file for easy parsing into the FishNet / other nets.

#### Requirements

Simply install the requirements below.
- [Python 2.7 32-bit](https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi)
- [Pygame 1.9 32-bit](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)

Then fork / clone this repo to your desktop. Then put your images into 
a 0001.jpg, 0002.jpg, etc format for training.

#### Usage

Ensure that python is added to path and that pygame is installed by running the following:
``` bash
python
>>> import pygame
>>>
```
If this does not throw any error, you're good to go! Run the script with the command below

``` bash
python trainer.py path/to/photos/ output.csv starting_index mode
```

Your output file with be comma separated, and ready to import to FishNet
