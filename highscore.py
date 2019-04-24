import highscoredata
from tkinter import *



class highscore:
    def __init__(self,path):
        self.highscorelist = highscoredata.highscorelist(path)
        self.root=Tk()
        
    def check(self, score):
        data = self.highscorelist.load()
        
        def handlename(name,highscorelist):
            print(name)
            self.root.quit()
        
        if data[0]['Score'] < score:
            playername=StringVar()
            Label(self.root, text='enter name').pack()
            Entry(self.root, textvariable=playername).pack()
            Button(self.root, text='Ok', command=lambda:handlename(playername.get(),self.highscorelist)).pack()
        
            self.root.mainloop()

if __name__ == "__main__":
	highscore = highscore('highscore.txt')
	
	
	
	highscore.check(1000)
