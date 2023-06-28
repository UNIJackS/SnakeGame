

import pygame
import time

intial_screen_width = 400

intial_screen_height = 200



pygame.init()

screen = pygame.display.set_mode((intial_screen_width,intial_screen_height))

game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)

time.sleep(50)


quit()