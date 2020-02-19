import pygame,time
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
    
    def __init__(self,username):
        self.username = username
    
    def getRunwayPrice(self):
        if self.runway < 8:
            price = 200000 + self.runway * self.runway * 50000
            return price
        else:
            return 0

    def buyRunway(self):
        price = self.getRunwayPrice()
        if price > 0 and self.money >= price:
            self.money -= price
            self.runway += 1
            return 1
        elif price == 0:
            return 2
        elif self.money < price:
            return 0
        else:
            return 3
    
    def addMoney(self,number):
        self.money += number

    def reduceMoney(self,number):
        self.money -= number

    def addContract(self,company):
        self.contract.append(company)

    def reduceContract(self,id):
        for c in range(len(self.contract)):
            if self.contract[c].id == id:
                del self.contract[c]
                break
                

class company:
    def __init__(self):
        self.id = time.time()