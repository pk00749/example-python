#! /usr/bin/python
# using sprites_rgba.png from http://img17.imageshack.us/img17/3166/spritesrgba.png
import sys, pygame, math, os, random
from pygame.locals import *
pygame.init()

size=width,height=1024,256;
screen=pygame.display.set_mode(size);

pygame.display.set_caption("multiplayer sprite test with collisions")

spd=4;
amnt=4;
ampl=8;

xpos=[0]*amnt;
ypos=[0]*amnt;
sprid=[];
spridr=[]   #some arrays and variables

for i in range (0,amnt,1):
  xpos[i]=64+(128*i)+random.randint(0,32);
  ypos[i]=64+random.randint(0,32)
  
sprall=pygame.image.load("sprites_rgba.png")  #loading sprites

for i in range (0,4,1):
  spritetmp=sprall.subsurface(0,0,64,64);#(refence,refence,width,height)
  spriterecttmp=spritetmp.get_rect()
  sprid.append(spritetmp); #append是列表的函数，表示在已有列表中加入一个新的成员
  spridr.append(spriterecttmp)
  
while 1:
  key=pygame.key.get_pressed()  #checking pressed keys
  if key[pygame.K_a]:xpos[0]-=spd
  if key[pygame.K_d]:xpos[0]+=spd
  if key[pygame.K_w]:ypos[0]-=spd
  if key[pygame.K_s]:ypos[0]+=spd
  if key[pygame.K_f]:xpos[1]-=spd
  if key[pygame.K_h]:xpos[1]+=spd
  if key[pygame.K_t]:ypos[1]-=spd
  if key[pygame.K_g]:ypos[1]+=spd
  if key[pygame.K_j]:xpos[2]-=spd
  if key[pygame.K_l]:xpos[2]+=spd
  if key[pygame.K_i]:ypos[2]-=spd
  if key[pygame.K_k]:ypos[2]+=spd
  if key[pygame.K_LEFT]: xpos[3]-=spd
  if key[pygame.K_RIGHT]:xpos[3]+=spd
  if key[pygame.K_UP]:   ypos[3]-=spd
  if key[pygame.K_DOWN]: ypos[3]+=spd
  
  bgcolour=0x998877    #checking collisions
  
  if spridr[0].colliderect(spridr[1]):bgcolour=0xAA5555
  if spridr[0].colliderect(spridr[2]):bgcolour=0x55AA55
  if spridr[0].colliderect(spridr[3]):bgcolour=0x5555AA
  if spridr[1].colliderect(spridr[2]):bgcolour=0x55AAAA
  if spridr[1].colliderect(spridr[3]):bgcolour=0xAA55AA
  if spridr[2].colliderect(spridr[3]):bgcolour=0xAAAA55
  screen.fill(bgcolour)
  
  for i in range (0,amnt,1):    #displaying sprites
    spridr[i].left=xpos[i];
    spridr[i].top=ypos[i];
    screen.blit(sprid[i],spridr[i])
    
  for event in pygame.event.get():  #praxis stuff
    if event.type==pygame.QUIT:sys.exit()
    
  pygame.display.flip();

  pygame.time.delay(1000/50)
