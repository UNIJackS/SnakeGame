

import pygame
import time
import sys
from pygame.locals import QUIT

SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

INITAL_SCREEN_WIDTH = 400
INITAL_SCREEN_HEIGHT = 200

inital_snake_x = (INITAL_SCREEN_WIDTH-SNAKE_WIDTH)/2
inital_snake_y = (INITAL_SCREEN_HEIGHT-SNAKE_HEIGHT)/2

SNAKE_RED = (245,54,34)
FOOD_BLUE = (127,202,255)
BACKROUND = (118,30,138)


pygame.init()

#Makes the inital page and sets its height and width to their intial values  and allows it to be resized
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)

#inports the awatapu logo and displays is as the icon of the program 
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)

#Sets the windows name to the string in this case Jacks snake game
pygame.display.set_caption("Jacks Snake game")


pygame.draw.rect(screen, SNAKE_RED, [inital_snake_x, inital_snake_y, SNAKE_WIDTH, SNAKE_HEIGHT])



#Infinte loop that loops until the exit button is pressed in the window 
quit_game = False
while not quit_game:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

pygame.quit()
quit()