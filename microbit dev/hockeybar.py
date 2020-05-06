import time
import utime
import random 
import microbit
from microbit import *

i=8

cs = pin8

spi.init()
bb1=pin0
bb2=pin1
bb3=pin2
bb4=pin5
bb5=pin11

def initleds():
    global i,cs
    for command, data in (
        (12, 0),  #  shutdown register 0 = shut off leds, remember state
        (15, 0),
        (11, 7),  #  scan limit register, Enable 8 colums of 8 leds
        (9, 0),
        (12, 1),  #  shutdown register, must be 1
        (10,1)): #  led brigthness

        for _ in range(8):
            spi.write(bytearray([command, data]))
            
        cs.write_digital(0)
        cs.write_digital(1)
      
def playintro():  
    for x in range(10):
        if (x % 2)==0:
            data=0b11111111
        else:
            data=0b00000000
        
        for y in range(8):
            for _ in range(i):
                spi.write(bytearray([1+y, data]))
            cs.write_digital(0)
            cs.write_digital(1)

        sleep(200)

def showscore(score):  
    rows = score // 8
    rest = score % 8
    for y in range(8):
        for _ in range(i):
            if y+1 <= rows:
                spi.write(bytearray([1+y,0b11111111]))
            elif y == rows:
                data = 0b00000001
                for _ in range(rest-1):
                    data = data << 1
                    data += 1
                    
                spi.write(bytearray([1+y,data]))
            else:
                spi.write(bytearray([1+y,0b00000000]))
                
        cs.write_digital(0)
        cs.write_digital(1)

        
def settarget(lasttarget=None):
    targetlist=[1,2,3,4,5]
    if lasttarget is not None:
        targetlist.remove(lasttarget)
    target=random.choice(targetlist)
    for y in range(8):
        for d in range(i):
            if d+1 == target:
                spi.write(bytearray([1+y, 255]))
            else:
                spi.write(bytearray([1+y, 0]))
        cs.write_digital(0)
        cs.write_digital(1)
    return target
    
def dimmtarget(target,brigtness):
    for y in range(8):
        if y+1 == target:
            spi.write(bytearray([10, brigtness-1]))

            cs.write_digital(0)
            cs.write_digital(1)
    return brigtness

def startgame():
    while True:
        if not bb1.read_digital() or not bb2.read_digital() or not bb3.read_digital() or not bb4.read_digital()  or not bb5.read_digital():  
            gamestate = "started"
            target = settarget()
            startticks = utime.ticks_ms()
            return gamestate,target,startticks


gamestatde="ready"
hitcount = 0

initleds()

playintro()

gamestate,target,startticks = startgame()

lastticks = startticks

microbit.display.scroll(gamestate, wait=False, loop=True)

currentb = 15

while not gamestate == "finished":
    if gamestate == "ready":
        gamestate,target,startticks = startgame()

    elif gamestate == "started":
        if target == 1 and not bb1.read_digital() or target == 2 and not bb2.read_digital() or target == 3 and not bb3.read_digital() or target == 4 and not bb4.read_digital() or target == 5 and not bb5.read_digital():
            target = settarget(target)
            hitcount += 1
    
    currentticks = utime.ticks_ms()
    if currentb > 0 and utime.ticks_diff(currentticks,lastticks) >= 500:
        #currentb = dimmtarget(target,currentb)
        lastticks = currentticks
    elif currentb == 0:
        target = settarget(target)
        currentb = 15
        
    if utime.ticks_diff(utime.ticks_ms(),startticks) >= 30000:
        gamestate = "finished"
        showscore(hitcount)
        microbit.display.scroll(gamestate, wait=False, loop=True)
           


