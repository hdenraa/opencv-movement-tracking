import time
import microbit
from microbit import *


b=pin0
microbit.display.set_pixel(4,4, 9)
while True:
    # microbit.display.scroll(str(pin.value()))
    if b.read_digital(): #pin0.read_digital():
        microbit.display.set_pixel(2,2, 5)
    else:
        microbit.display.set_pixel(2,2, 0)
        microbit.display.set_pixel(4,4, 0)
    time.sleep(0.1)
