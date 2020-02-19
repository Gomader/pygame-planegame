import pygame,sys,mouse,screen
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60
time = 0

if __name__ == "__main__":
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:#I have test this place, when we start another loop in other files' function here the function will be no effect
                sys.exit()

        time += 1

        mode = screen.md

        screen.set_screen(mode,time)

        mouse.intmouse(screen.screen)

        pygame.display.update()