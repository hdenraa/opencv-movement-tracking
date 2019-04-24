import cv2
#import cv2.cv as cv
import numpy as np
import pygame
import math
import random
import os.path
import pickle
import cProfile
import time
#import pyglet
from kallibrer0512 import kallibrer
from findcircle_blob0512  import circleposition
from spriteclasses  import Player,Block,Border,BLACK,WHITE,GREEN,RED,BLUE
from puckmovement  import puck_movement
from random import randint
import copy

    
def main():
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("/home/lars/dev/Videos/Webcam/2017-12-20-223500.webm")
    #window = pyglet.window.Window()
    #cursor= window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
    #window.set_mouse_cursor(cursor)

        
    pygame.init()
     
    # Set the height and width of the screen
    screen_width = 1513
    screen_height = 900
    fullscreen = pygame.display.set_mode([screen_width, screen_height],pygame.FULLSCREEN)
    
    screen = pygame.Surface((1510,842))
    gameoutput = pygame.Surface((1510,58))
    
    screen.fill(WHITE)
    gameoutput.fill(RED)
     
    myfont = pygame.font.SysFont("monospace", 30,True)


    player = Player(BLACK, 60, 60)
    topborder = Border(BLACK, 20, 142, 745,0)
    bluehole = Border(BLUE, 20,142, 745,142)
    midborder = Border(BLACK, 20, 274, 745,284)
    redhole = Border(RED, 20, 142, 745, 557)
    lowborder = Border(BLACK, 20, 142, 745,699)
 

    targettl = Border(GREEN, 120, 120,312,220)
    targetbl = Border(GREEN, 120, 120,312,500)
    targettr = Border(GREEN, 120, 120,1077,220)
    targetbr = Border(GREEN, 120, 120,1077,500)

    targets = [targettl,targetbl,targettr,targetbr]
    
    sprite_list = pygame.sprite.Group()
    target_list = pygame.sprite.Group()

    sprite_list.add(player)
    target = copy.copy(targets[randint(0,3)])

    sprite_list.add(redhole)
    sprite_list.add(bluehole)
    sprite_list.add(topborder)
    sprite_list.add(midborder)
    sprite_list.add(lowborder)
    
    sprite_list.add(targets)

    target_list.add(targets)


    # -------- Main Program Loop -----------
    start_ticks=pygame.time.get_ticks()

    started = False 
    done = False    
    score=0

    dest = np.array([ [0,0],[1299,0],[1299,699],[0,699] ],np.float32)
    
    myfont = pygame.font.SysFont("monospace", 30,True)
        
    time1 = time.clock()

    x=0
    dircount = 0
    pucksizelist = []
    
    while True: 
        screen.fill(WHITE)
        sprite_list.draw(screen)
        
        pygame.draw.line(gameoutput, BLACK, (0,58), (1512,58))
        

        Score = myfont.render("Count ", 1, (0,50,0))
        Hole = myfont.render("Hole ", 1, (0,50,0))
        
        #screen.blit(Timecount,(10,10))        
        gameoutput.blit(Score,(10,20))
        gameoutput.blit(Hole,(200 ,20))
        
        fullscreen.blit(gameoutput,(0,0))
        fullscreen.blit(screen,(0,59))
        
        cv2.waitKey(10)
        #if timelimit <= 0:
        #    return hitcount
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return
        
        pygame.display.update()        
        # = time.clock()
        #if x>100:
        #s    break
    #with open("pucksizelist","wb") as f: 
    #    pickle.dump(pucksizelist,f)
#cProfile.run('main()')

#while True:
main()
    #resultscreen(hitcount)

#while not    

pygame.quit()
