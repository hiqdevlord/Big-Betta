""" FishNet Trainer Application

    Usage > python trainer.py path/to/photos/ output/path index mode

    Example python trainer.py images learning.csv 1 activity

"""

import pygame
import sys, os, os.path
from pygame.locals import *
from util import *

# Parse command line args
if len(sys.argv) != 5:
    print 'Incorrect Command line args'
    print 'Usage > python trainer.py path/to/photos/ output/path index mode'
    exit()

photo_path = sys.argv[1]
outfile = sys.argv[2]
img_index =  int(sys.argv[3])
mode = sys.argv[4]

total_pics = len(os.listdir(photo_path))

# Get first image
image = get_image(photo_path, img_index)


# Initialize Pygame
pygame.init()
pygame.font.init()

# Define colors
BLACK = (  0,   0,   0)
BLUE  = (  0, 191, 235)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
# Set the height and width of the screen
screen_width = image.get_width()
screen_height = image.get_height()
grid_x = 10
grid_y = 10

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('FishNet Trainer') 
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

# Init font stuff
text_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
text_surf = background.convert_alpha()
text_surf.fill((255,255,255,0))

if pygame.font:
    font = pygame.font.Font(None, 36)

text = font.render('Image '+str(img_index)+' of '+str(total_pics), True, WHITE)
textpos = text.get_rect(centerx=150)

text_surf.blit(text, textpos)



# Generate Grid Lines
grid = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
grid = background.convert_alpha()
grid.fill((255,255,255,0))

for x in xrange(0,screen_width, screen_width/grid_x):
    pygame.draw.aaline(grid, BLUE, (x,0), (x,screen_height))

for y in xrange(0, screen_height, screen_height/grid_y):
    pygame.draw.aaline(grid, BLUE, (0,y), (screen_width,y))


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()



f = open(outfile, 'wb')
output_data = []

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            print 'FINISHED LEARNING, K THX BAI\n Writing to file...'
            f.writelines(output_data)

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                print 'FINISHED LEARNING, K THX BAI\n Writing to file...'
                f.writelines(output_data)
                done = True

            elif event.key == pygame.K_SPACE:

                # Convert position to 1D output vector
                location = 0
                
                output_data.append(str(img_index).zfill(4)+'.jpg , '+str(location)+'\n')

                img_index += 1
                image = get_image(photo_path, img_index)

                # Update our label
                text_surf.fill((255,255,255,0))
                text = font.render('Image '+str(img_index)+' of '+str(total_pics), True, WHITE)
                textpos = text.get_rect(centerx=150)
                text_surf.blit(text, textpos)
                

                # You're done looking at images, WRITE IT TO A FILE
                if image is None:
                    print 'FINISHED LEARNING, K THX BAI\n Writing to file...'
                    f.writelines(output_data)
                    quit()

            elif mode == 'activity' and pygame.K_0 <= event.key <= pygame.K_9:
                output_data.append(str(img_index).zfill(4)+'.jpg , '+str(event.key-48)+'\n')

                img_index += 1
                image = get_image(photo_path, img_index)

                # Update our label
                text_surf.fill((255,255,255,0))
                text = font.render('Image '+str(img_index)+' of '+str(total_pics), True, WHITE)
                textpos = text.get_rect(centerx=150)
                
                text_surf.blit(text, textpos)
                

                # You're done looking at images, WRITE IT TO A FILE
                if image is None:
                    print 'FINISHED LEARNING, K THX BAI\n Writing to file...'
                    f.writelines(output_data)
                    done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == 'position':
                
                # Convert position to 1D output vector
                pos = event.pos
                location = pos[0]*grid_x/screen_width+pos[1]*grid_y/screen_height*grid_y
                
                output_data.append(str(img_index).zfill(4)+'.jpg , '+str(location)+'\n')

                img_index += 1
                image = get_image(photo_path, img_index)

                # Update our label
                text_surf.fill((255,255,255,0))
                text = font.render('Image '+str(img_index)+' of '+str(total_pics), True, WHITE)
                textpos = text.get_rect(centerx=150)
                text_surf.blit(text, textpos)
                

                # You're done looking at images, WRITE IT TO A FILE
                if image is None:
                    print 'FINISHED LEARNING, K THX BAI\n Writing to file...'
                    f.writelines(output_data)
                    quit()

    # Clear the screen
    screen.fill(BLACK)



    # Blit stuff
    screen.blit(background, (0,0))
    screen.blit(image, (0,0))

    if mode == 'position':
        screen.blit(grid, (0,0))

    screen.blit(text_surf, (0,screen_height-30))
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()