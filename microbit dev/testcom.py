from pygame import joystick, key
from pygame.locals import *
import sys, serial, time
from random import randint
import re
import serial.tools.list_ports

ports = list( serial.tools.list_ports.comports(True) )
port = "/dev/ttyACM0"
for p in ports:
	if p.description == 'DAPLink CMSIS-DAP - mbed Serial Port':
	   port = p.device


baud = 115200
sumx = 0
sumy = 0  
count=0  

    
s = serial.Serial(port)
s.baudrate = baud
#s.parity = serial.PARITY_NONE
#s.databits = serial.EIGHTBITS
#s.stopbits = serial.STOPBITS_ONE
data = s.readline()
#time.sleep(0.1)
data = str(data)
print(data)
mbit = False
tr = 200 #treshold 

if "x, y, z:" in data:
	mbit = True
	#count += 1 
	split = data.split(":")[-1].split()
	print(split)
	x = int(split[0])
	y = int(split[1])
	z = int(re.sub('[^-0-9]', '',split[2]))
	#print("New x, y, z:", x, y, z)
 
