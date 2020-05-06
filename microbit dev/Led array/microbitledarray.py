from microbit import *

class Matrix:
    def __init__(self, cs):
        self.cs = cs
        self.buffer = bytearray(8)
        spi.init()
        self.init()

    def _register(self, command, data):       
        self.cs.write_digital(0)
        spi.write(bytearray([command, data]))
        self.cs.write_digital(1)
        
    def _registerlhp(self, command, data):       
        spi.write(bytearray([command, data]))
 
    def init(self):
        for command, data in (
            (12, 0),
            (15, 0),
            (11, 7),
            (9, 0),
            (12, 1),
        ):
            self._register(command, data)

    def brightness(self, value):
        self._register(10, value)

    def fill(self, color): 
        data=0x100 if color else 0x00
        for y in range(8):
            self.buffer[y] = data

    def pixel(self, x, y, color=None):
        if color is None:
            return bool(self.buffer[y] & 1 << x)
        elif color:
            self.buffer[y] |= 1 << x
        else:
            self.buffer[y] &= ~(1 << x)

    def show(self):
        for y in range(8):
            self._register(1 + y, self.buffer[y])

d = Matrix(pin8)
d.brightness(15)
d.show()


d.show()
      
sleep(10000)
  
        
for x in range(8):
   for y in range(8):
      d.pixel(x,y,False)
      d.show()    

sleep(10000) 
      
for x in range(8):
   for y in range(8):
      d.pixel(x,y,True)
      d.show()

sleep(10000)    

for x in range(8):
   for y in range(8):
      d.pixel(x,y,False)
      d.show()   
       
