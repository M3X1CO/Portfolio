import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('WHY DO WE NEED WINDOWS')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (100, 150, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 48)
fontObj.set_bold(True)  # Set the font style as bold
textSurfaceObj = fontObj.render('Hello World', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
