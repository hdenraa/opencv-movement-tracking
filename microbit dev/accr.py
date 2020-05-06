#uflash file.py

from microbit import *
import radio

radio.on()

display.clear()
display.scroll("acc recieve alive")

while True:
    message = radio.receive()
    if message:
		print(message)
    
