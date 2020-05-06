from microbit import *

cs = pin8
data = bytearray(1)
spi.init()
  
i=8

for command, data in (
    (12, 0),
    (15, 0),
    (11, 7),
    (9, 0),
    (12, 1),
    (10,15)
):

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

    
# ~ sleep(1000)

# ~ for y in range(8):
    # ~ cs.write_digital(0)
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ cs.write_digital(1)
        
# ~ sleep(1000)

# ~ for y in range(8):
    # ~ cs.write_digital(0)
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ spi.write(bytearray([1+y, 255]))
    # ~ cs.write_digital(1)

# ~ sleep(1000)

# ~ for y in range(8):
    # ~ cs.write_digital(0)
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ spi.write(bytearray([1+y, 0]))
    # ~ cs.write_digital(1)


for y in range(8):
    for _ in range(i):
        spi.write(bytearray([1+y, 255]))
    cs.write_digital(0)
    cs.write_digital(1)

sleep(1000)

for m in range(8):
    for x in [254,253,251,247,239,223,191,127]:
        for y in range(8):
            for _ in range(i-1):
               spi.write(bytearray([1+y, 255]))
            spi.write(bytearray([1+y, x]))
            for _ in range(m):
                spi.write(bytearray([1+y, 255]))
            cs.write_digital(0)
            cs.write_digital(1)
        sleep(500)

# ~ for x in [254,253,251,247,239,223,191,127]:
    # ~ for y in range(8):
        # ~ for _ in range(i-2):
           # ~ spi.write(bytearray([1+y, 255]))
        # ~ spi.write(bytearray([1+y, x]))
        # ~ spi.write(bytearray([1+y, 255]))
        # ~ cs.write_digital(0)
        # ~ cs.write_digital(1)
    # ~ sleep(500)

# ~ for x in [254,253,251,247,239,223,191,127]:
    # ~ for y in range(8):
        # ~ for _ in range(i-2):
           # ~ spi.write(bytearray([1+y, 255]))
        # ~ spi.write(bytearray([1+y, x]))
        # ~ spi.write(bytearray([1+y, 255]))
        # ~ spi.write(bytearray([1+y, 255]))
        # ~ cs.write_digital(0)
        # ~ cs.write_digital(1)
    # ~ sleep(500)
