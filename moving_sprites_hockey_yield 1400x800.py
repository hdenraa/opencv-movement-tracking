import cv2
import cv2.cv as cv
import numpy as np
import pygame
import random

cap = cv2.VideoCapture(1)
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Loop until the user clicks the close button.


def puck_movement():
    done = False
    l=[[1,1],[1,1],[1,1]]
    start_ticks=pygame.time.get_ticks()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill(WHITE)
    
        puckx = 200
        pucky = 350
    
        ret, frame = cap.read()
        fframe=cv2.flip(frame,0)
        ffframe=cv2.flip(fframe,1)

        gray = cv2.cvtColor(ffframe, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        circles = cv2.HoughCircles(blur,cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=5,minRadius=15,maxRadius=22)
    
        if circles is not None:
            for circle in circles[0]:
                if np.absolute(circle[0]*2-l[2][0]) > 5 or np.absolute(circle[1]*2-l[2][1]) > 5:
                    l.append([circle[0]*2,circle[1]*2])
                    l=l[1:]
                break
    
        yield l[2]
    
class Border(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height,xpos,ypos):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Border,self).__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.height = height
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        print "gygag"
        self.rect.y = -self.height-100
 
    def update(self,puckx,pucky):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 2
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 100+self.height:
            self.reset_pos()
     
 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Block,self).__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-700, -20)
        self.rect.x = random.choice([random.randrange(0,1400)])
 
    def update(self,puckx,pucky):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 810:
            self.reset_pos()
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor
		super(Player,self).__init__()

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		pygame.draw.circle(self.image, color, (width/2,height/2),min(width,height)/2, 0)
		
		#self.image.fill(color)

		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
        
    def update(self,puckx,pucky):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = puckx
        self.rect.y = pucky
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
started = False

myfont = pygame.font.SysFont("monospace", 30,True)


player = Player(BLACK, 30, 30)
# -------- Main Program Loop -----------
prev_blocks_hit_list = None
start_ticks=pygame.time.get_ticks()


def startscreen(score):

    global screen
    started = False
    
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    

    all_sprites_list.add(player)
    startBlock = Block(GREEN, 60, 60)
    all_sprites_list.add(startBlock)
    startBlock.rect.x = 630
    startBlock.rect.y = 320
    block_list.add(startBlock)
    all_sprites_list.draw(screen)
    

    while not started:
        for puck in puck_movement():
            
            player.update(puck[0],puck[1])
            
            all_sprites_list.draw(screen)     
            
            Score = myfont.render("Score to beat:"+str(score), 1, (0,50,0))
            screen.blit(Score,(10,10))
            # See if the player block has collided with anything.
            clock.tick(20)
            pygame.display.flip()
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False,pygame.sprite.collide_rect)
            #if blocks_hit_list is not None:
            for block in blocks_hit_list:
                print("HIT!!!!!")
                started = True
                return

 
# Create a puck block

#border1 = Border(BLUE,30,300,200,-250)
#border2 = Border(BLUE,30,300,200,150)
#border3 = Border(BLUE,30,300,500,-150)
#border4 = Border(BLUE,30,300,500,250)

#all_sprites_list.add(border1)
#all_sprites_list.add(border2) 
#all_sprites_list.add(border3)
#all_sprites_list.add(border4) 
#block_list.add(border1)
#block_list.add(border2) 
#block_list.add(border3)
#block_list.add(border4)

started = False 
done = False    
score=0
while not done:
    startscreen(score)
    score=0
    start_ticks=pygame.time.get_ticks()

    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
     
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    
    for i in range(50):
        # This represents a block
        block = Block(RED, 50, 50)
     
        # Set a random location for the block
        block.rect.x = random.choice([random.randrange(0,1400)])
        block.rect.y = random.randrange(screen_height)
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)


    for puck in puck_movement():
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
 
        if seconds >= 30:
            break
        print (seconds)
         
        # Calls update() method on every sprite in the list
        all_sprites_list.update(puck[0],puck[1])
     
        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False,pygame.sprite.collide_rect)
        if prev_blocks_hit_list == blocks_hit_list:
            pass
        else:
            for block in blocks_hit_list:
                if type(block) is Block:
                    score += 1
                    print(score)
                    block.reset_pos()
                    print type(block)
                elif type(block) is Border:
                    score -= 20
                    print type(block)
                else:
                    print type(block)

        prev_blocks_hit_list = blocks_hit_list

        Score = myfont.render("Score:"+str(score), 1, (0,50,0))
        gametime = myfont.render("Time:"+str(30-seconds), 1, (0,50,0))

        # Draw all the spites
        all_sprites_list.draw(screen)
        screen.blit(Score,(10,10))
        screen.blit(gametime,(10,40))
        # Limit to 20 frames per second
        clock.tick(20)
     
        # Go ahead and update the screen with what we've drawn.
        
        pygame.display.flip()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    
    
pygame.quit()
