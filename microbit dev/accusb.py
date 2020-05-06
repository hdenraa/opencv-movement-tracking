#uflash file.py

from microbit import *

display.clear()
display.scroll("acc alive")

while True:
    #g = accelerometer.current_gesture()
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    print("x, y, z:" + str(x) + " " + str(y) + " " + str(z))
