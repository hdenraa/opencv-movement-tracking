from tkinter import *
import pygame
import random
import os
import time
root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
embed = Frame(root) #, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
embed.grid(row=0,column=0, sticky='news')
#embed.pack(side = LEFT)
#embed.lower()
buttonwin = Frame(root) #width = 75, height = 500)
buttonwin.grid(row=0,column=0, sticky='news')
def hide():
    embed.tkraise()
    embed.pack(expand=1)
    root.update()
    # ~ time.sleep(3)
    # ~ buttonwin.tkraise()
    # ~ root.update()
#buttonwin.pack(side = LEFT)
button1 = Button(buttonwin,text = 'Draw', command = hide)
button1.pack(side=LEFT)
buttonwin.tkraise()
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

