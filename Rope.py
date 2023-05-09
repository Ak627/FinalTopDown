import pygame
import random
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

class rope:
    def __init__(self):
        self.xpos = 480
        self.ypos = 200
        self.direction = RIGHT
        self.ticker = 0
    def draw(self, screen, xoff, yoff):
        pygame.draw.circle(screen, (250, 0, 250), (self.xpos+xoff, self.ypos+yoff), 20)

    def move(self, map,  px, py, xoff, yoff):
        self.ticker +=1 
        #check if player is direct line of sight
        #print("y positions in grid:", int(py/50),int(self.ypos/50))
        if int(py/50) == int(self.ypos/50): #check that player and rope are in same row
            if px < self.xpos: #check that player is to the right of rope
                #print("I SEE YOU", end = " ")
                if map[int((self.ypos ) / 50)][int( (self.xpos +30 )  / 50)] !=2:
                    self.xpos+=5
            elif px > self.xpos: #left
                if map[int((self.ypos ) / 50)][int( (self.xpos )  / 50)] !=2:
                    self.xpos-=5
        #you need to expand this for the other directions

        #otherwise randomly wander
        elif self.ticker%40==0:
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
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +30 )  / 50)] ==2:
            #print("bumped right!")
            self.direction = UP
        if self.direction == LEFT and map[int((self.ypos) / 50)][int( (self.xpos - 5 )  / 50)] ==2:
            #print("bumped left!")
            self.direction = DOWN
        if self.direction == UP and map[int((self.ypos - 5 ) / 50)][int( (self.xpos )  / 50)] ==2:
            #print("bumped up!")
            self.direction = LEFT
        if self.direction == DOWN and map[int((self.ypos + 30 ) / 50)][int( (self.xpos  )  / 50)] ==2:
            #print("bumped down!")
            self.direction = RIGHT

        #or actually move!
        elif self.direction == RIGHT:
                self.xpos += 1
        elif self.direction == LEFT:
                self.xpos -= 1
        elif self.direction == UP:
                self.ypos -= 1
        else:
                self.ypos +=4
               
