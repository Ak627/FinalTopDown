import pygame
import random
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
mino = pygame.image.load('Minotaur.png') #load your spritesheet
class rope:
    def __init__(self):
        self.xpos = 480
        self.ypos = 200
        self.width = 50
        self.height = 50
        self.frameNum = 0
        self.RowNum = 0
        self.health = 100
        
        
        self.direction = RIGHT
        self.ticker = 0
        
        self.movingx = True
        self.movingy = True
    def draw(self, screen, xoff, yoff):
        if self.movingx == True or self.movingy == True: #animate when moving
            self.ticker+=1
        if self.ticker % 30 == 0: #only change frames every 10 ticks
            self.frameNum+=1
        if self.frameNum > 3: 
            self.frameNum = 0
        
        pygame.draw.rect(screen, (250, 0, 250), (self.xpos+xoff, self.ypos+yoff, self.width, self.height))
        screen.blit(mino, (self.xpos+xoff, self.ypos +yoff), (self.width * self.frameNum, self.RowNum * self.height, self.width, self.height))
        
        
    def move(self, map,  px, py, xoff, yoff):
        self.ticker +=1 
        #check if player is direct line of sight
        print("y positions in grid:", int(py/50),int(self.ypos/50))
        if int(py/50) == int(self.ypos/50): #check that player and rope are in same row
            
            if px > self.xpos: #check that player is to the rigth of rope
                print("I SEE YOU, AND IM GOING RIGHT",  end = " ")
                if map[int((self.xpos  + 50) / 50)][int( (self.ypos)  / 50)] !=2:
                    self.direction = RIGHT
                    self.xpos+=5
                else:
                    self.xpos += 0
            elif px < self.xpos: #left
                print("I SEE YOU, AND IM GOING LEFT", end = " ")
                if map[int((self.ypos ) / 50)][int( (self.xpos)  / 50)] !=2:
                    self.direction = LEFT
                    self.xpos-=5
                else:
                    self.xpos += 0
                    
                    
        #you need to expand this for the other directions
        if int(px/50) == int(self.xpos/50): #check that player and rope are in same collumn
            if py < self.ypos:
                print("I SEE YOU, AND IM GOING ", self.direction, end = " ")
                if map[int((self.xpos ) / 50)][int( (self.ypos  + 50)  / 50)] !=2:
                    self.direction = UP
                    self.ypos-=5
            elif py > self.ypos:
                print("I SEE YOU, AND IM GOING ", self.direction, end = " ")
                if map[int((self.xpos ) / 50)][int( (self.ypos)  / 50)] !=2:
                    self.direction = DOWN
                    self.ypos+=5
                    
        #otherwise randomly wander
        elif self.ticker%20==0:
            num = random.randrange(0, 4)
            if num == 0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction == UP
            else:
                self.direction = DOWN

        #check for collision and change direction if you've bumped
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +self.width )  / 50)] ==2 or self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +self.width )  / 50)] ==3:
            #print("bumped right!")
            self.direction = UP
        if self.direction == LEFT and map[int((self.ypos) / 50)][int( (self.xpos - 5 )  / 50)] ==2 or self.direction == LEFT and  map[int((self.ypos) / 50)][int( (self.xpos - 5 )  / 50)] ==3:
            #print("bumped left!")
            self.direction = DOWN
        if self.direction == UP and map[int((self.ypos - 5 ) / 50)][int( (self.xpos )  / 50)] ==2 or self.direction == UP and map[int((self.ypos - 5 ) / 50)][int( (self.xpos )  / 50)] ==3:
            #print("bumped up!")
            self.direction = LEFT
        if self.direction == DOWN and map[int((self.ypos + self.height ) / 50)][int( (self.xpos  )  / 50)] ==2 or self.direction == DOWN and map[int((self.ypos + self.height ) / 50)][int( (self.xpos  )  / 50)] ==3:
            #print("bumped down!")
            self.direction = RIGHT

        #or actually move!
        elif self.direction == RIGHT:
                self.RowNum = 2
                self.xpos += 2
        elif self.direction == LEFT:
                self.RowNum = 3
                self.xpos -= 2
        elif self.direction == UP:
                self.RowNum = 1
                self.ypos -= 2
        else:
                self.RowNum = 0
                self.ypos +=2
               
