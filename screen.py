import pygame,sys,classes,images
from pygame.locals import *
import rgbcolorlist as color

pygame.init()

pygame.display.set_caption("Amazing Airport")

screen = pygame.display.set_mode((1080,720),0,32)

md = 0

def set_screen(mode,time):
    if mode == 0:
        start_action(time)
    elif mode == 1:
        new_game()
        

def start_action(time):
    if time<=20:
        screen.blit(images.start_action1,(0,0))
    elif time<=25:
        screen.blit(images.start_action2,(0,0))
    elif time<=30:
        screen.blit(images.start_action3,(0,0))
    elif time<=35:
        screen.blit(images.start_action4,(0,0))
    elif time<=40:
        screen.blit(images.start_action5,(0,0))
    elif time<=45:
        screen.blit(images.start_action6,(0,0))
    elif time<=50:
        screen.blit(images.start_action7,(0,0))
    elif time<=55:
        screen.blit(images.start_action8,(0,0))
    elif time<=60:
        screen.blit(images.start_action9,(0,0))
    elif time<=65:
        screen.blit(images.start_action10,(0,0))
    else:
        screen.blit(images.start_actionmain,(0,0))
        homepage_btn()
            
def homepage_btn():
    pygame.draw.rect(screen,[199,150,111],[440,350,200,50],0)
    test = classes.text("New Game",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(test.getImage(),(460,355))
    pygame.draw.rect(screen,[199,150,111],[440,450,200,50],0)
    test = classes.text("Loading",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(test.getImage(),(490,455))
    pygame.draw.rect(screen,[199,150,111],[440,550,200,50],0)
    test = classes.text("Exit",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(test.getImage(),(500,555))
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if(x>=430 and x<=650 and y>=340 and y<=410):
                test = classes.text("New Game",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(test.getImage(),(460,355))
                global md 
                md = 1
            elif(x>=430 and x<=650 and y>=440 and y<=510):
                test = classes.text("Loading",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(test.getImage(),(490,455))
            elif(x>=430 and x<=650 and y>=540 and y<=610):
                test = classes.text("Exit",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(test.getImage(),(500,555))
                sys.exit()

def new_game():
    screen.blit(images.normal_background,(0,0))