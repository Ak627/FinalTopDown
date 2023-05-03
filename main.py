import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((832, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
SPACE = 4


class player:
    def __init__(self, x_offset, y_offset):
        self.xpos = 400
        self.ypos = 400
        self.vx = 0
        self.vy = 0
        self.pWidth = 32
        self.pHeight = 46
        self.hp = 100
        self.isAlive = True
        self.swordAlive = False
        self.xoffset = x_offset
        self.yoffset = y_offset
        
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.xpos > 400:
                self.vx = -3
            elif self.xoffset < 0:
                self.xoffset += 3
                self.vx = 0
            RowNum = 0
        
        elif keys[pygame.K_RIGHT]:
            if self.xpos<400:
                self.vx=3
            elif self.xoffset>-800:
                self.xoffset-=3
                self.vx = 0
            RowNum = 1
            
        else:
            self.vx = 0
            
        if keys[pygame.K_DOWN]:
            if self.ypos<400:
                self.vy=3
            elif self.yoffset>-800:
                self.yoffset -=3
                self.vy = 0
            RowNum = 1
            RowNum = 3
        
        elif keys[pygame.K_UP]:
            if self.ypos > 400:
                self.vy = -3
            elif self.yoffset<0:
                self.yoffset +=3
                self.vy = 0
            RowNum = 0
            RowNum = 2

        else:
            self.vy = 0
            
        self.xpos += self.vx
        self.ypos += self.vy
        
    def collision(self, gameMap):
        print("Checking position: ", int((self.ypos-self.yoffset+self.pHeight)/50) , int((self.xpos-self.xoffset+self.pWidth/2)/50))
        #print("Positions are: ", self.xpos, self.ypos)
        #print("Offsets are: ", self.xoffset, self.yoffset)
        
        #down collision
        if gameMap[int((self.ypos-self.yoffset+self.pHeight)/50)][int((self.xpos-self.xoffset+self.pWidth/2)/50)]==2 or gameMap[int((self.ypos-self.yoffset+self.pHeight)/50)][int((self.xpos-self.xoffset+self.pWidth/2)/50)]==3:
            self.ypos-=3
        #up collision
        if gameMap[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+self.pWidth/2)/50)]==2 or gameMap[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+self.pWidth/2)/50)]==3:
            self.ypos+=3     
        #left collision
        if gameMap[int((self.ypos-self.yoffset+self.pHeight-10)/50)][int((self.xpos-self.xoffset-10)/50)]==2 or gameMap[int((self.ypos-self.yoffset+self.pHeight-10)/50)][int((self.xpos-self.xoffset-10)/50)]==3:
            self.xpos+=3
        #right collision
        if gameMap[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+self.pWidth+5)/50)]==2 or gameMap[int((self.ypos-self.yoffset)/50)][int((self.xpos-self.xoffset+self.pWidth+5)/50)]==3:
            self.xpos-=3
            
        
        #stop moving if you hit edge of screen (will be removed for scrolling)
        if self.xpos+self.pWidth > 800:
            self.xpos-=3
        if self.xpos<0:
            self.xpos+=3
            
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
    def draw(self, dire):
        pygame.draw.rect(screen, (0,0,0), (20, 20, 100, 15))
        pygame.draw.rect(screen, (255,0,0), (20,20, self.hp, 15))
        if self.swordAlive == True:
            if dire == RIGHT:
                pygame.draw.rect(screen, (175, 175, 175), (self.xpos + 30, self.ypos + 20, 20,5))
                pygame.draw.polygon(screen, (175, 175, 175), ((self.xpos+50, self.ypos + 20), (self.xpos+50, self.ypos+25), (self.xpos+55, self.ypos +22.5) ))
            elif dire == LEFT:
                pygame.draw.rect(screen, (175, 175, 175), (self.xpos-20, self.ypos + 20, 20,5))
                pygame.draw.polygon(screen, (175, 175, 175), ((self.xpos-20, self.ypos+20), (self.xpos-20, self.ypos+25), (self.xpos-25, self.ypos +22.5)))
            if dire == DOWN:
                pygame.draw.rect(screen, (175, 175, 175), (self.xpos, self.ypos + 40, 5,20))
                pygame.draw.polygon(screen, (175, 175, 175), ((self.xpos, self.ypos+60), (self.xpos+5, self.ypos+60), (self.xpos+2.5, self.ypos +65)))
            elif dire == UP:
                pygame.draw.rect(screen, (175, 175, 175), (self.xpos, self.ypos-10, 5,20))
                pygame.draw.polygon(screen, (175, 175, 175), ((self.xpos, self.ypos-10), (self.xpos+5, self.ypos-10), (self.xpos+2.5, self.ypos -15)))
        if self.isAlive == True:
            screen.blit(Link, (self.xpos, self.ypos), (self.pWidth*frameNum, RowNum*self.pHeight, self.pWidth, self.pHeight))
            
    



#gameMap: 1 is grass, 2 is tree
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2 ,0 ,0, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0 ,0 ,2, 2,2],
       [2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 2,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 3, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 3, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 3, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,3, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 3,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 2, 3, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0 ,2 ,2, 0,2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2]]

tree = pygame.image.load('Bamboo.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
rock = pygame.image.load('Dwayne.png')
grass = pygame.image.load('Grass.png')
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
# xpos = 400 #xpos of player
# ypos = 400 #ypos of player
# vx = 0 #x velocity of player
# vy = 0 #y velocity of player
x_offset = 0
y_offset = 0
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
movingx = False
movingy = False

#animation variables variables
frameWidth = 32
frameHeight = 46
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

p1 = player(x_offset, y_offset)

while not gameover:
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

         

    p1.move()
        
       
    
    p1.attack()

    

    if p1.health() == False:
        gameover = True
   
    #COLLISION
     #down collision
       
       
       
    p1.collision(map)


    #ANIMATION-------------------------------------------------------------------
       
    # Update Animation Information

    if movingx == True or movingy == True: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7:
           frameNum = 0
 
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((51,117,70)) #wipe screen so it doesn't smear
   
    #draw gameMap
    for i in range (28):
        for j in range(33):
            if map[i][j]==0:
                screen.blit(grass, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(tree, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(rock, (j*50+x_offset, i*50+y_offset), (0, 0, 50, 50))
        
    #draw player
    p1.draw(direction)
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()

