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
    for x in range(11):
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
 
    
def dimmtarget(b):
    for y in range(8):
        spi.write(bytearray([10, b]))

    cs.write_digital(0)
    cs.write_digital(1)


initleds()

playintro()

currentb = 15
stop= False
while not stop:
    dimmtarget(currentb)
    for y in range(8):
        for _ in range(i):
            spi.write(bytearray([1+y, 0b11111111]))
        cs.write_digital(0)
        cs.write_digital(1)
        
    currentb = currentb - 1
    time.sleep(1)
    if currentb == -1:
        stop=True
