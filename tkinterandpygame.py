from tkinter import *
import pygame
import random
import os
import time
root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
embed = Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
embed.grid(row=0,column=2)
#embed.pack(side = LEFT)
#embed.lower()
buttonwin = Frame(root, width = 75, height = 500)
def hide():
    buttonwin.pack_forget()
    root.update()
    time.sleep(3)
    buttonwin.pack()
#buttonwin.pack(side = LEFT)
button1 = Button(buttonwin,text = 'Draw', command = hide)
button1.pack(side=LEFT)
embed.lift(buttonwin)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'x11'
pygame.display.init()
screen = pygame.display.set_mode((root.winfo_screenwidth(), root.winfo_screenheight()))
pygame.display.flip()
while True:
    #your code here
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.flip()
    root.update()

