

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

#Sets the windows name to the string in this case Jacks snake game
pygame.display.set_caption("Jacks Snake game")

#Infinte loop that loops until the exit button is pressed in the window 
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

pygame.quit()
quit()