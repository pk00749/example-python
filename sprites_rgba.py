#! /usr/bin/python
# using sprites_rgba.png from http://img17.imageshack.us/img17/3166/spritesrgba.png
import sys, pygame, math, os, random
from pygame.locals import *
pygame.init()
size=width,height=960,240;screen=pygame.display.set_mode(size);pygame.display.set_caption("multiplayer sprite test with collisions")
spd=4;amnt=4;ampl=8;xpos=[0]*amnt;ypos=[0]*amnt;rotv=[0]*amnt;sprid=[];spridr=[]   #some arrays and variables
for i in range (0,amnt,1):
  xpos[i]=64+(128*i)+random.randint(0,32);
  ypos[i]=64+random.randint(0,32);
  rotv[i]=random.randint(0,359)
sprall=pygame.image.load("sprites_rgba.png")  #loading sprites
for i in range (0,4,1):
  spritetmp=sprall.subsurface(i*64,0,64,64);
  spriterecttmp=spritetmp.get_rect()
  sprid.append(spritetmp);
  spridr.append(spriterecttmp)
rotincr=5
while 1:
  key=pygame.key.get_pressed()  #checking pressed keys
  if key[pygame.K_a]:xpos[0]-=spd
  if key[pygame.K_d]:xpos[0]+=spd
  if key[pygame.K_w]:ypos[0]-=spd
  if key[pygame.K_s]:ypos[0]+=spd
  if key[pygame.K_z]:rotv[0]+=rotincr
  if key[pygame.K_x]:rotv[0]-=rotincr
  if key[pygame.K_f]:xpos[1]-=spd
  if key[pygame.K_h]:xpos[1]+=spd
  if key[pygame.K_t]:ypos[1]-=spd
  if key[pygame.K_g]:ypos[1]+=spd
  if key[pygame.K_v]:rotv[1]+=rotincr
  if key[pygame.K_b]:rotv[1]-=rotincr
  if key[pygame.K_j]:xpos[2]-=spd
  if key[pygame.K_l]:xpos[2]+=spd
  if key[pygame.K_i]:ypos[2]-=spd
  if key[pygame.K_k]:ypos[2]+=spd
  if key[pygame.K_m]:rotv[2]+=rotincr
  if key[pygame.K_COMMA]:rotv[2]-=rotincr
  if key[pygame.K_LEFT]: xpos[3]-=spd
  if key[pygame.K_RIGHT]:xpos[3]+=spd
  if key[pygame.K_UP]:   ypos[3]-=spd
  if key[pygame.K_DOWN]: ypos[3]+=spd
  if key[pygame.K_KP0]:  rotv[3]+=rotincr
  if key[pygame.K_KP_PERIOD]:rotv[3]-=rotincr
  bgcolour=0x998877    #checking collisions
  if spridr[0].colliderect(spridr[1]):bgcolour=0xAA5555
  if spridr[0].colliderect(spridr[2]):bgcolour=0x55AA55
  if spridr[0].colliderect(spridr[3]):bgcolour=0x5555AA
  if spridr[1].colliderect(spridr[2]):bgcolour=0x55AAAA
  if spridr[1].colliderect(spridr[3]):bgcolour=0xAA55AA
  if spridr[2].colliderect(spridr[3]):bgcolour=0xAAAA55
  screen.fill(bgcolour)
  for i in range (0,amnt,1):    #displaying sprites
    spridr[i].centerx=xpos[i]
    spridr[i].centery=ypos[i]
    tmq=pygame.transform.rotate(sprid[i],rotv[i])
    screen.blit(tmq,spridr[i])
  for event in pygame.event.get():  #praxis stuff
    if event.type==pygame.QUIT:sys.exit()
  pygame.display.flip();pygame.time.delay(1000/50)
