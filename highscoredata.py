import pickle
import os.path
import json


class highscorelist:
	def __init__(self,path):
		self.path = path
		
	def update(self,entry):
		current = self.load()
		
		current.append(entry)
		
		print(current)
		
		highscore_list=sorted(current,key=lambda entry1:entry1['Score'],reverse=True)
		
		print(highscore_list)
		
		self.save(highscore_list)
		
	def load(self):
		if os.path.isfile(self.path):
			highscore_list = pickle.load(open( self.path, "rb" )) 
		else:
			highscore_list = []
		return highscore_list
			
	def save(self,highscore_list):
		pickle.dump(highscore_list,open( self.path,"wb" )) 

	
	
if __name__ == "__main__":
	import cv2
	import time
	cap = cv2.VideoCapture(0)
	done = False 
	
	while not done:
		ret, frame = cap.read()
		
		frame= cv2.flip(frame,1)
		
		height,width,channels = frame.shape
		
		print("{},{}".format(width,height))
		
		pwidth = width/2
		pheight = height/1.2
		
		ulx = int(width/2-pwidth/2) 
		uly = int(height/2-pheight/2)
		brx = int(width/2+pwidth/2)
		bry = int(height/2+pheight/2)
		
		cv2.rectangle(frame,(ulx,uly),(brx,bry),(0,255,0),5)
		
		cv2.imshow('frame',frame)
		fframe = frame.copy()

		if cv2.waitKey(1) & 0xFF == ord('q'):
			done = True
			
	fframe = frame[uly:bry,ulx:brx]		

	cv2.imshow('fframe',fframe)
	cv2.waitKey(100)
	time.sleep(5)
    
	cv2.imwrite("face.jpg",frame)
	highscore_list = highscorelist("highscore.txt")
	highscore_list.update({'Name':'hest','Score':31,'Pic':'face.pic'})
	print(highscore_list.load())
	
	cap.release()
	cv2.quit()
