# Add your Python code here. E.g.
from microbit import *


while True:
    if accelerometer.was_gesture('up'):
        display.clear()
        display.scroll("Dogs cannot look up")
        print("up")
        sleep(100)
        
    elif accelerometer.was_gesture('down'):
        display.clear()
        display.scroll("I feel sick")
        print("down")
        sleep(100)
        
    elif accelerometer.was_gesture('left'):
        display.clear()
        display.scroll("Left")
        print("left")
        sleep(100)

    elif accelerometer.was_gesture('right'):
        display.clear()
        display.scroll("Right")
        print("right")
        sleep(100)

    elif accelerometer.was_gesture('shake'):
        display.clear()
        print("shake")
        display.scroll("Stop shaking me!")
        sleep(100)


