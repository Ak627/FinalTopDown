import pygame
#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4


Po = pygame.image.load('Po Souls.png') #load your spritesheet
Po.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

class player:
    def __init__(self):
      #player variables
      self.xpos = 400 #xpos of player
      self.ypos = 400 #ypos of player
      self.vx = 0 #x velocity of player
      self.vy = 0 #y velocity of player
      self.xoffset = 0
      self.yoffset = 0  
      self.movingx = False
      self.movingy = False
      
      self.swordAlive =  False
      self.isAlive = True
      self.hp = 100
      #animation variables variables
      self.frameWidth = 32
      self.frameHeight = 46
      self.RowNum = 0 #for left animation, this will need to change for other animations
      self.frameNum = 0
      self.ticker = 0
      self.direction = DOWN
      
      
      self.ticker = 0 
    def draw(self,screen):
        if self.movingx == True or self.movingy == True: #animate when moving
            self.ticker+=1
        if self.ticker % 10 == 0: #only change frames every 10 ticks
            self.frameNum+=1
        if self.frameNum > 3: 
            self.frameNum = 0
        
        #health bar
        if self.hp > 60: 
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, self.hp, 20))
        elif self.hp  > 40:
            pygame.draw.rect(screen, (255, 255, 0), (20, 20, self.hp, 20))
        elif self.hp > 0:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, self.hp, 20))    
        pygame.draw.rect(screen, (0,0,0), (20, 20, 100, 20), 5)
        
        
        #sword
        if self.swordAlive == True:
            if self.direction == RIGHT:
                pygame.draw.rect(screen, (212, 139, 4), (self.xpos + 20, self.ypos + 20, 30,5))
            elif self.direction == LEFT:
                pygame.draw.rect(screen, (212, 139, 4), (self.xpos-20, self.ypos + 20, 30,5))
            if self.direction == DOWN:
                pygame.draw.rect(screen, (212, 139, 4), (self.xpos+3, self.ypos + 23, 5,30))
            elif self.direction == UP:
                pygame.draw.rect(screen, (212, 139, 4), (self.xpos + 23, self.ypos-13, 5,30))
        #player   
        if self.isAlive == True:
            screen.blit(Po, (self.xpos, self.ypos), (self.frameWidth * self.frameNum, self.RowNum * self.frameHeight, self.frameWidth, self.frameHeight)) 
        return self.ticker
    
    
    
    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
                self.swordAlive = True
        else:
            self.swordAlive = False
            
    def health(self):
        if self.hp <= 0:
            self.isAlive = False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_k]:
                self.hp -= 1
        elif keys[pygame.K_p]:
            self.hp += 10
            if self.hp >= 100:
                self.hp = 100
        return self.isAlive
    
    def move(self, keys, map):

        if keys[LEFT] == True:
            if self.xpos > 400:
                self.vx = -3
                self.RowNum = 0
                self.direction = LEFT
                self.movingx = True
            elif self.xoffset < 0:
                self.xoffset+=3
                self.vx = 0
                self.RowNum = 0
                self.direction = LEFT
                self.movingx = True
            else:
                self.vx = -3
                self.RowNum = 0
                self.direction = LEFT
                self.movingx = True
        
        #RIGHT MOVEMENT
        elif keys[RIGHT] == True:
            if self.xpos < 400:
                self.vx = 3
                self.RowNum = 1
                self.direction = RIGHT
                self.movingx = True
            elif self.xoffset > -800:
                self.xoffset-=3
                self.vx = 0
                self.RowNum = 1
                self.direction = RIGHT
                self.movingx = True
            else:
                self.vx = 3
                self.RowNum = 1
                self.direction = RIGHT
                self.movingx = True
        #turn off velocity
        else:
            self.vx = 0
            self.movingx = False



        
    #DOWN MOVEMENT
        if keys[DOWN] == True:
            if self.ypos < 400:
                self.vy = 3
                self.RowNum = 1
                self.RowNum = 3
                self.direction = DOWN
                self.movingy = True
            elif self.yoffset > -800:
                self.yoffset-=3
                self.vy = 0
                self.RowNum = 1
                self.RowNum = 3
                self.direction = DOWN
                self.movingy = True
            else:
                self.vy = 3
                self.RowNum = 1
                self.RowNum = 3
                self.direction = DOWN
                self.movingy = True

         #UP MOVEMENT
        elif keys[UP] == True:
            if self.ypos > 400:
                self.vy = -3
                self.RowNum = 0
                self.RowNum = 2
                self.direction = UP
                self.movingy = True
            elif self.yoffset < 0:
                self.yoffset+=3
                self.vy = 0
                self.RowNum = 0
                self.RowNum = 2
                self.direction = UP
                self.movingy = True
            else:
                self.vy = -3
                self.RowNum = 0
                self.RowNum = 2
                self.direction = UP
                self.movingy = True
        #turn off velocity
        else:
            self.vy = 0
            self.movingy = False
            

    
    #COLLISION
    
    #down collision
        if map[int((self.ypos - self.yoffset + self.frameHeight) / 50)][int((self.xpos - self.xoffset + self.frameWidth / 2) / 50)] == 2 or map[int((self.ypos - self.yoffset + self.frameHeight) / 50)][int((self.xpos - self.xoffset + self.frameWidth / 2) / 50)] == 3:
            self.ypos-=3
    
    #up collision
        if map[int((self.ypos - self.yoffset) / 50)][int((self.xpos - self.xoffset + self.frameWidth / 2) / 50)] == 2 or map[int((self.ypos - self.yoffset) / 50)][int((self.xpos - self.xoffset + self.frameWidth / 2) / 50)] == 3:
            self.ypos+=3
        
    #left collision
        if map[int((self.ypos - self.yoffset + self.frameHeight - 10) / 50)][int((self.xpos - self.xoffset - 10) / 50)] == 2 or map[int((self.ypos - self.yoffset + self.frameHeight - 10) / 50)][int((self.xpos - self.xoffset - 10) / 50)] == 3:
            self.xpos+=3
        
    #right collision
        if map[int((self.ypos - self.yoffset) / 50)][int((self.xpos - self.xoffset + self.frameWidth + 5) / 50)] == 2 or map[int((self.ypos - self.yoffset) / 50)][int((self.xpos - self.xoffset + self.frameWidth + 5) / 50)] == 3:
            self.xpos-=3    

    #stop moving if you hit edge of screen (will be removed for scrolling)
        if self.xpos + self.frameWidth > 800:
            self.xpos-=3
        if self.xpos < 0:
            self.xpos+=3

        self.xpos+=self.vx #update player xpos
        self.ypos+=self.vy

