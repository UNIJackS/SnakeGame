from sre_constants import RANGE
from turtle import Screen
import pygame
import time
import sys
import random
import math
from pygame.locals import QUIT

SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

INITAL_SCREEN_WIDTH = 1000
INITAL_SCREEN_HEIGHT = 720

snake_pos = [((math.trunc(INITAL_SCREEN_WIDTH/SNAKE_WIDTH))/2*SNAKE_WIDTH), ((math.trunc(INITAL_SCREEN_HEIGHT/SNAKE_HEIGHT))/2*SNAKE_HEIGHT)]

food_pos = [0,0]

food_alive = True

SNAKE_RED = (245,54,34)
FOOD_BLUE = (127,202,255)
BACKROUND = (0,0,0)
LIGHT_BACROUND = (118,30,138)

clock = pygame.time.Clock()

TICK_TIME = 10


pygame.init()

pygame.key.set_repeat(0)


#Makes the inital page and sets its height and width to their intial values  and allows it to be resized
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)

#inports the awatapu logo and displays is as the icon of the program 
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)

#Sets the windows name to the string in this case Jacks snake game
pygame.display.set_caption("Jacks Snake game")

font = pygame.font.Font("freesansbold.ttf", 50)

def message(msg,text_colour, bkgd_colour):
    txt = font.render(msg, True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center = (INITAL_SCREEN_WIDTH/2, INITAL_SCREEN_HEIGHT/2))
    screen.blit(txt, text_box)

#Draws the backround elements
def backround_drawing():
    #Fills the backround with the bacround colour
    screen.fill(BACKROUND)

    #Drawers the grid for the backround
    for x in range(math.trunc(INITAL_SCREEN_WIDTH/SNAKE_WIDTH)):
        for y in range(math.trunc(INITAL_SCREEN_HEIGHT/SNAKE_HEIGHT)):
            pygame.draw.rect(screen,LIGHT_BACROUND,[x*SNAKE_WIDTH+1,y*SNAKE_HEIGHT+1,18,18])


def input_checker():
    snake_delta_x = 0
    snake_delta_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                snake_delta_x = -SNAKE_WIDTH
                snake_delta_y = 0

            elif event.key == pygame.K_RIGHT:
                snake_delta_x = SNAKE_WIDTH
                snake_delta_y = 0

            elif event.key == pygame.K_UP:
                snake_delta_y = -SNAKE_HEIGHT
                snake_delta_x = 0

            elif event.key == pygame.K_DOWN:
                snake_delta_y = SNAKE_HEIGHT
                snake_delta_x = 0

    return [snake_delta_x,snake_delta_y]



#Infinte loop that loops until the exit button is pressed in the window 
quit_game = False

while not quit_game:
    
    #checks if there has been user input and exacutes apprprate movement
    snake_pos_delta = input_checker()
    #moves snake in x axis
    snake_pos[0] += snake_pos_delta[0]
    #moves snake in y axis
    snake_pos[1] += snake_pos_delta[1]


    #quits game if you go outside the intial bounds 
    if snake_pos[0] >= INITAL_SCREEN_WIDTH or snake_pos[0] < 0 or snake_pos[1] >= INITAL_SCREEN_HEIGHT or snake_pos[1] < 0:
        quit_game = True

    if (snake_pos[0]+10 == food_pos[0] and snake_pos[1]+10 == food_pos[1]):
        food_alive = True
    
    #draws backround elements
    backround_drawing()

    pygame.draw.rect(screen, SNAKE_RED, [snake_pos[0], snake_pos[1], SNAKE_WIDTH, SNAKE_HEIGHT])
    
    #checks if the food is alive if not spawns a new one
    if(food_alive == True):
        food_pos[0] = (SNAKE_WIDTH*random.randint(1, ((math.trunc(INITAL_SCREEN_WIDTH/SNAKE_WIDTH)))))-SNAKE_WIDTH/2
        food_pos[1] = (SNAKE_HEIGHT*random.randint(1, ((math.trunc(INITAL_SCREEN_HEIGHT/SNAKE_HEIGHT)))))-SNAKE_HEIGHT/2

        food_alive = False
    
    #draws the food hexagons
    pygame.draw.polygon(screen, FOOD_BLUE, ((food_pos[0]-10,food_pos[1]+5),(food_pos[0]-10,food_pos[1]-5),(food_pos[0],food_pos[1]-10),(food_pos[0]+10,food_pos[1]-5),(food_pos[0]+10,food_pos[1]+5),(food_pos[0],food_pos[1]+10)))

    

    pygame.display.update()

    clock.tick(TICK_TIME)

        
message ("You died!", BACKROUND, SNAKE_RED)
pygame.display.update()
time.sleep(3)


pygame.quit()
quit()