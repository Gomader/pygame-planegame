import pygame,sys
from pygame.locals import *

white = 255,255,255
blue = 0,0,200
mouse_image_filename = "images/mouse.png"
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello",True,white)
pygame.display.set_caption("Amazing Airport")
mouse_cursor = pygame.image.load(mouse_image_filename)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(0,0))
    x, y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))

    pygame.display.update()