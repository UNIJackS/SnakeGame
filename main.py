# Workbook pages 37 - 54.
# Copy your code into the various snake_vx files as you
# reach those check points.
# Edit the code that is below as needed.


import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()