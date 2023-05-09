import pygame
import math
from Player import player
from Octo import octo
from Rope import rope

pygame.init()  
pygame.display.set_caption("Final Game")  # sets the window title
screen = pygame.display.set_mode((832, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4



#gameMap: 1 is grass, 2 is bamboo, 3 is rock
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2 ,0 ,0, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2 ,2 ,2, 2,2],
       [2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0 ,0 ,2, 2,2],
       [2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 2,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 3, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 3, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
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

bamboo = pygame.image.load('Bamboo.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
rock = pygame.image.load('Dwayne.png')
grass = pygame.image.load('Grass.png')
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
keys = [False, False, False, False, False] #this list holds whether each key has been pressed

#animation variables variables
ticker = 0
direction = DOWN

p1 = player()
octos = []
for i in range(5):
    octos.append(octo())



while not gameover:
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
         

    p1.move(keys, map)
    for i in range(len(octos)):
        octos[i].move(map, p1.xpos+p1.xoffset, p1.ypos+p1.yoffset, p1.xoffset, p1.yoffset)
        p1.hp = octos[i].collision(p1.xpos, p1.ypos, p1.xoffset, p1.yoffset, p1.frameWidth, p1.frameHeight, p1.swordAlive, p1.hp)
    p1.attack()
    if p1.health() == False:
        gameover = True

       
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((51,117,70)) #wipe screen so it doesn't smear
   
    #draw gameMap
    for i in range (28):
        for j in range(33):
            if map[i][j]==0:
                screen.blit(grass, (j*50+p1.xoffset, i*50+p1.yoffset), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(bamboo, (j*50+p1.xoffset, i*50+p1.yoffset), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(rock, (j*50+p1.xoffset, i*50+p1.yoffset), (0, 0, 50, 50))
        
    #draw player
    p1.draw(screen)
    for i in range(len(octos)):
        octos[i].draw(screen,  p1.xoffset, p1.yoffset)
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()

