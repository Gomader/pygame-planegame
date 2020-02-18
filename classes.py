import pygame
from pygame.locals import *

class text:

    inner = ''
    family = ''
    color = 0,0,0
    size = 0

    def __init__(self,inner,size,color,family=None):
        self.inner = inner
        self.family = family
        self.size = size
        self.color = color

    def getImage(self):
        myfont = pygame.font.Font(self.family,self.size)
        textImage = myfont.render(self.inner,True,self.color)
        return textImage


class game:

    username = ''
    money = 1000000
    contract = []
    runway = 1
    
