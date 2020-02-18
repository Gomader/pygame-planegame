import pygame,sys,mouse,screen
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60
time = 0
mode = 0

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    time += 1

    screen.set_screen(mode,time)

    mouse.intmouse(screen.screen)

    pygame.display.update()