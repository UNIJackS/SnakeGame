

import pygame
import time
import sys
from pygame.locals import QUIT


intial_screen_width = 400
intial_screen_height = 200

pygame.init()

#Makes the inital page and sets its height and width to their intial values  and allows it to be resized
screen = pygame.display.set_mode((intial_screen_width,intial_screen_height), pygame.RESIZABLE)

#inports the awatapu logo and displays is as the icon of the program 
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)


#Infinte loop that loops until the exit button is pressed in the window 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


quit()