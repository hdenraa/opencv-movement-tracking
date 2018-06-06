import cv2
import cv2.cv as cv
import numpy as np
import pygame
import math
import random
import os.path
import pickle
import cProfile
import time
import pyglet
from kallibrer import kallibrer
from findcircle_blob import circleposition
from spriteclasses import Player,Block,Border,BLACK,WHITE,GREEN,RED,BLUE
from puckmovement import puck_movement
from random import randint
import copy

def main():
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("/home/lars/Videos/Webcam/2017-12-20-223500.webm") 
    window = pyglet.window.Window()
    cursor= window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
    window.set_mouse_cursor(cursor)

        

     
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

    targettl = Border(GREEN, 120, 120,265,115)
    targetbl = Border(GREEN, 120, 120,265,415)
    targettr = Border(GREEN, 120, 120,915,115)
    targetbr = Border(GREEN, 120, 120,915,415)

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
    
    sprite_list.add(target)

    target_list.add(target)


    # -------- Main Program Loop -----------

    start_ticks=pygame.time.get_ticks()

    started = False 
    done = False    
    score=0

    dest = np.array([ [0,0],[1299,0],[1299,699],[0,699] ],np.float32)
    
    undistinfo = pickle.load(open("undistinfo.p","rb"))
    mtx = undistinfo['mtx']
    dist = undistinfo['dist']
    ret, frame = cap.read()
    h,  w = frame.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    
    warp,mask,maskcorners,_ = kallibrer(cap,dest,newcameramtx,mtx,dist)
    dircount = 0
    hole = ""
    print "am alive"
    myfont = pygame.font.SysFont("monospace", 30,True)
        
    time1 = time.clock()
    start_ticks = pygame.time.get_ticks()
    x=0
    hitcount=0
    for puck in puck_movement(lambda:circleposition(cap,warp,newcameramtx,mtx,dist,mask,maskcorners)):
        time2 = time.clock()
        print 'clocktime %0.6f' % (time2-time1)     
        #time1=time2   
        x+=1
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
        
        target_hit_list = pygame.sprite.spritecollide(player, target_list, True,pygame.sprite.collide_rect)
            #if blocks_hit_list is not None:
        for target in target_hit_list:
            print("HIT!!!!!")
            target = copy.copy(targets[randint(0,3)])
            hitcount+=1
            sprite_list.add(target)
            target_list.add(target)
        

        # Draw all the spites
        #screen.blit(player.image,player.rect)
        # Limit to 20 frames per second
        #clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        Time = myfont.render("Time "+ str(30-seconds), 1, (0,50,0))
        Hole = myfont.render("Hit count "+ str(hitcount), 1, (0,50,0))
                
        screen.blit(Time,(10,10))
        screen.blit(Hole,(10,30))
        
        pygame.display.flip()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time1 = time.clock()
        #if x>100:
        #s    break
#cProfile.run('main()')

main()    
    
pygame.quit()
