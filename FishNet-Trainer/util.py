import pygame
import os


_image_library = {}
def get_image(path, index):
        global _image_library
        path = path+'\\'+str(index).zfill(4)+'.jpg'
        print path
        image = _image_library.get(path)
        if image == None:
            try:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
            except:
                return None
        index += 1
        return image

