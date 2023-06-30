import pygame
import time
import sys
from pygame.locals import QUIT

SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

INITAL_SCREEN_WIDTH = 400
INITAL_SCREEN_HEIGHT = 200

snake_x = (INITAL_SCREEN_WIDTH-SNAKE_WIDTH)/2
snake_y = (INITAL_SCREEN_HEIGHT-SNAKE_HEIGHT)/2

snake_delta_x = 0
snake_delta_y = 0

SNAKE_RED = (245,54,34)
FOOD_BLUE = (127,202,255)
BACKROUND = (118,30,138)

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


time_since_last_input = 0


#Infinte loop that loops until the exit button is pressed in the window 
quit_game = False
while not quit_game:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


        pygame.draw.rect(screen, SNAKE_RED, [0, 0, SNAKE_WIDTH, SNAKE_HEIGHT])
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

        snake_x += snake_delta_x
        snake_y += snake_delta_y

        time_since_last_input = time.time()

        screen.fill(BACKROUND)

        pygame.draw.rect(screen, SNAKE_RED, [snake_x, snake_y, SNAKE_WIDTH, SNAKE_HEIGHT])
        pygame.display.update()

        clock.tick(TICK_TIME)




pygame.quit()
quit()