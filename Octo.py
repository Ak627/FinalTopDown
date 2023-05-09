import pygame
import random
enemy = pygame.image.load("EnemyO.png")
#directions
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3



class octo:
    def __init__(self):
        self.xpos = random.randrange(0,800)
        self.ypos = random.randrange(0,800)
        self.vx = 0
        self.vy = 0
        self.height = 26
        self.width = 26
        self.RowNum = 0
        self.frameNum = 0
        
        self.xoffset = 0
        self.yoffset = 0
        self.ticker = 0
        self.choice = 0
        self.direction = LEFT
        self.isAlive = True
        
        self.aniticker = 0
        self.movingx = False
        self.movingy = False
#         self.bulletAlive = False
#         self.Bx = self.xpos + 13
#         self.By = self.ypos + 13
#         self.Bvx = 0
#         self.Bvy = 0
        
    def move(self, map, px, py, xoff, yoff):
        self.ticker += 1
        if int(self.ticker)%100 == 0:
            self.choice = random.randrange(0,6)
            #left
            if self.choice == 0:
                self.direction = LEFT
                self.movingx = True
            #right
            elif self.choice == 1:
                self.direction = RIGHT
                self.movingx = True
            #up
            elif self.choice == 2:
                self.direction = UP
                self.movingy = True
            #down
            elif self.choice == 3:
                self.direction = DOWN
                self.movingy = True
            
#             elif self.choice == 4:
#                 self.Bvx = 0
#                 self.Bvy = 0
#                 octo.shoot(self)
            else:
                self.Bvx = 0
                self.Bvy = 0
        
        
        
        
        
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +30 )  / 50)] ==2 or self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +30 )  / 50)] ==3:
            #print("bumped right!")
            self.direction = UP
        if self.direction == LEFT and map[int((self.ypos) / 50)][int( (self.xpos - 5 )  / 50)] ==2 or self.direction == LEFT and  map[int((self.ypos) / 50)][int( (self.xpos - 5 )  / 50)] ==3:
            #print("bumped left!")
            self.direction = DOWN
        if self.direction == UP and map[int((self.ypos - 5 ) / 50)][int( (self.xpos )  / 50)] ==2 or self.direction == UP and map[int((self.ypos - 5 ) / 50)][int( (self.xpos )  / 50)] ==3:
            #print("bumped up!")
            self.direction = LEFT
        if self.direction == DOWN and map[int((self.ypos + 30 ) / 50)][int( (self.xpos  )  / 50)] ==2 or self.direction == DOWN and map[int((self.ypos + 30 ) / 50)][int( (self.xpos  )  / 50)] ==3:
            #print("bumped down!")
            self.direction = RIGHT

        #or actually move!
        elif self.direction == RIGHT:
                self.frameNum = 1
                self.xpos += 1
        elif self.direction == LEFT:
                self.frameNum = 0
                self.xpos -= 1
        elif self.direction == UP:
                self.frameNum = 2
                self.ypos -= 1
        else:
                self.frameNum = 3
                self.ypos +=1

        
        
        self.xpos += self.vx
        self.ypos += self.vy
        
#         if self.choice != 4:
#             self.Bx = self.xpos + 13
#             self.By = self.ypos + 13
#         
#     def shoot(self):
#         self.bulletAlive = True
#         
#         if self.direction == LEFT:
#             self.Bvx = -6
#         elif self.direction == RIGHT:
#             self.Bvx = 6
#             
#         if self.direction == UP:
#             self.Bvy = -6
#         elif self.direction == DOWN:
#             self.Bvy = 6
#         
#         self.Bx += self.Bvx
#         self.By += self.Bvy
        
    def collision(self, px, py, xoff, yoff, w, h, weapon, health):
        if self.isAlive == True:
            if (self.ypos + self.height) + yoff >= py and self.ypos + yoff <= py + h and (self.xpos + self.width) + xoff >= px and self.xpos + xoff <= px + w:
                print("is colliding")
                health -= 1
                
        return health
    def draw(self, screen, xoff, yoff):
#         if self.bulletAlive == True:
#             pygame.draw.rect(screen, (140, 118, 77), (self.Bx + xoff, self.By + yoff, 10, 10))

            
        if self.isAlive == True:
            screen.blit(enemy, (self.xpos + xoff, self.ypos + yoff), (self.width * self.frameNum, self.RowNum * self.height, self.width, self.height))
            
        