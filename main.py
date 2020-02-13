import pygame,sys
from pygame.locals import *

white = 255,255,255
blue = 0,0,200
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello",True,white)
pygame.display.set_caption("Amazing Airport")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(300,250))
    pygame.display.update()