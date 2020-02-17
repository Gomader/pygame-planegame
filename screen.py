import pygame,sys
from pygame.locals import *
import rgbcolorlist as color

pygame.init()

pygame.display.set_caption("Amazing Airport")

screen = pygame.display.set_mode((1080,720),0,32)
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello",True,color.white)
background1 = pygame.image.load("images/homepagegif/1.jpg")
background2 = pygame.image.load("images/homepagegif/2.jpg")
background3 = pygame.image.load("images/homepagegif/3.jpg")
background4 = pygame.image.load("images/homepagegif/4.jpg")
background5 = pygame.image.load("images/homepagegif/5.jpg")
background6 = pygame.image.load("images/homepagegif/6.jpg")
background7 = pygame.image.load("images/homepagegif/7.jpg")
background8 = pygame.image.load("images/homepagegif/8.jpg")
background9 = pygame.image.load("images/homepagegif/9.jpg")
background10 = pygame.image.load("images/homepagegif/10.jpg")
backgroundmain = pygame.image.load("images/homepagegif/main.jpg")

def set_screen(mode,time):
    if mode == 0:
        if time<=20:
            screen.blit(background1,(0,0))
        elif time<=25:
            screen.blit(background2,(0,0))
        elif time<=30:
            screen.blit(background3,(0,0))
        elif time<=35:
            screen.blit(background4,(0,0))
        elif time<=40:
            screen.blit(background5,(0,0))
        elif time<=45:
            screen.blit(background6,(0,0))
        elif time<=50:
            screen.blit(background7,(0,0))
        elif time<=55:
            screen.blit(background8,(0,0))
        elif time<=60:
            screen.blit(background9,(0,0))
        elif time<=65:
            screen.blit(background10,(0,0))
        else:
            screen.blit(backgroundmain,(0,0))
            pygame.draw.rect(screen,[255,0,0],[250,150,300,200],0)
