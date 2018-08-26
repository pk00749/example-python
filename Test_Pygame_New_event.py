#-*-coding=utf-8-*-
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
 
font = pygame.font.SysFont("arial", 16);

event_text = []
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
    
    
    CATONKEYBOARD = USEREVENT+1
    my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
    pygame.event.post(my_event)
     
    #然后获得它
    for event in pygame.event.get():
        if event.type == CATONKEYBOARD:
            print event.message
            print CATONKEYBOARD
            print USEREVENT
    
 
    pygame.display.update()
