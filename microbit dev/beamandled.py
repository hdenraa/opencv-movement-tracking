import time
import microbit
from microbit import *

i=8
cs = pin8
data = bytearray(1)
spi.init()

for command, data in (
    (12, 0),
    (15, 0),
    (11, 7),
    (9, 0),
    (12, 1),
    (10,15)):

    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    spi.write(bytearray([command, data]))
    cs.write_digital(0)
    cs.write_digital(1)
    
for y in range(8):
    for _ in range(i):
        spi.write(bytearray([1+y, 255]))
    cs.write_digital(0)
    cs.write_digital(1)
    
b=pin0

sleep(2000)

while True:
    # microbit.display.scroll(str(pin.value()))
    if b.read_digital(): #pin0.read_digital():
        for y in range(8):
            for _ in range(i):
                spi.write(bytearray([1+y, 0]))
            cs.write_digital(0)
            cs.write_digital(1)
    else:
        for y in range(8):
            for _ in range(i):
                spi.write(bytearray([1+y, 255]))
            cs.write_digital(0)
            cs.write_digital(1)
    time.sleep(0.1)

