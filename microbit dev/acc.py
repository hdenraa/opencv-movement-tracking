#uflash file.py

from microbit import *
import radio

radio.on()

display.clear()
display.scroll("acc alive")

while True:
    #g = accelerometer.current_gesture()
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    radio.send("x, y, z:" + str(x) + " " + str(y) + " " + str(z))
