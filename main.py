import pygame,sys,mouse,screen
from pygame.locals import *

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.set_screen()

    mouse.intmouse(screen.screen)

    pygame.display.update()