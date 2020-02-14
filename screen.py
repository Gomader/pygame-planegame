import pygame,sys
from pygame.locals import *
import rgbcolorlist as color

pygame.init()

pygame.display.set_caption("Amazing Airport")

screen = pygame.display.set_mode((400,650),0,32)
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello",True,color.white)

def set_screen():
    screen.fill(color.blue)
    screen.blit(textImage,(0,0))
