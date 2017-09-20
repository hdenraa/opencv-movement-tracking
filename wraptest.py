import cv2
import cv2.cv as cv
import numpy as np
import pygame
import math
import random
import os.path
import pickle
from kallibrer import kallibrer
from findcircle import circleposition
from spriteclasses import Player,Block,Border,BLACK,WHITE,GREEN,RED,BLUE
from puckmovement import puck_movement

cap = cv2.VideoCapture(1)
 



    

 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(WHITE)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
started = False

myfont = pygame.font.SysFont("monospace", 30,True)


player = Player(BLACK, 60, 60)
topborder = Border(BLACK, 20, 117, 640,0)
midborder = Border(BLACK, 20, 230, 640,235)
lowborder = Border(BLACK, 20, 117, 640,583)
bluehole = Border(BLUE, 20,117, 640,117)
redhole = Border(RED, 20, 117, 640, 466)

sprite_list = pygame.sprite.Group()

sprite_list.add(player)


sprite_list.add(redhole)
sprite_list.add(bluehole)
sprite_list.add(topborder)
sprite_list.add(midborder)
sprite_list.add(lowborder)
# -------- Main Program Loop -----------

start_ticks=pygame.time.get_ticks()

started = False 
done = False    
score=0

dest = np.array([ [0,0],[1299,0],[1299,699],[0,699] ],np.float32)

warp = kallibrer(cap,dest)
dircount = 0
hole = ""

myfont = pygame.font.SysFont("monospace", 30,True)

for puck in puck_movement(lambda:circleposition(cap,warp)):
    print "puck_movement for"
    
    # Calls update() method on every sprite in the list
    sprite_list.update(puck[0][2][0],puck[0][2][1])
    if puck[1]:
        dircount = dircount + 1

    if (puck[0][2][0] > 660 and puck[0][1][0] < 640) or (puck[0][2][0] < 640 and puck[0][1][0] > 660):
        if puck[0][2][1] > 350:
            hole = "Red"
        else:
            hole = "Blue"
        dircount = 0
        
    screen.fill(WHITE)
    sprite_list.draw(screen)

    # Draw all the spites
    #screen.blit(player.image,player.rect)
    # Limit to 20 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    
    Score = myfont.render("Count "+ str(dircount), 1, (0,50,0))
    Hole = myfont.render("Hole "+ str(hole), 1, (0,50,0))
            
    screen.blit(Score,(10,10))
    screen.blit(Hole,(10,30))
    
    pygame.display.flip()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    
    
pygame.quit()
