import pygame,sys,classes,images,time
from pygame.locals import *
import rgbcolorlist as color

pygame.init()

pygame.display.set_caption("Amazing Airport")

screen = pygame.display.set_mode((1080,720),0,32)

md = 0

name = ''

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
        homepage_btn()
            
def homepage_btn():
    screen.blit(images.start_actionmain,(0,0))
    pygame.draw.rect(screen,[199,150,111],[440,350,200,50],0)
    text = classes.text("New Game",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(text.getImage(),(460,355))
    pygame.draw.rect(screen,[199,150,111],[440,450,200,50],0)
    text = classes.text("Loading",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(text.getImage(),(490,455))
    pygame.draw.rect(screen,[199,150,111],[440,550,200,50],0)
    text = classes.text("Exit",40,color.white,"font/Crimes-Times-Six-1.ttf")
    screen.blit(text.getImage(),(500,555))
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if(x>=430 and x<=650 and y>=340 and y<=410):
                test = classes.text("New Game",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(text.getImage(),(460,355))
                global md 
                md = 1
            elif(x>=430 and x<=650 and y>=440 and y<=510):
                text = classes.text("Loading",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(text.getImage(),(490,455))
            elif(x>=430 and x<=650 and y>=540 and y<=610):
                text = classes.text("Exit",40,color.blue,"font/Crimes-Times-Six-1.ttf")
                screen.blit(text.getImage(),(500,555))
                sys.exit()

def new_game():
    screen.blit(images.normal_background,(0,0))
    text = classes.text("Add Your Name:",40,color.Chocolate4,"font/Crimes-Times-Six-1.ttf")
    screen.blit(text.getImage(),(400,300))
    event = pygame.event.poll()
    if event.type == KEYDOWN:
        global name
        print(event.key)
        if event.key == K_RETURN:
            text = classes.text("OK",40,color.white,"font/Crimes-Times-Six-1.ttf")
            screen.blit(text.getImage(),(500,500))
        elif event.key == K_BACKSPACE:
            name = name[:-1]
        else:
            name += chr(event.key)
        
    else:
      pass
    text = classes.text(name,40,color.white,"font/Crimes-Times-Six-1.ttf")
    x = 540 - len(name)*10
    screen.blit(text.getImage(),(x,450))