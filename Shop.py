import pygame
outside = pygame.image.load('Shop.png') #load your spritesheet
outside.set_colorkey((255,255,255))

wyno = pygame.image.load('WynoShop.png')



Inside = pygame.image.load(r'Inside.png')
Inside_size = Inside.get_rect().size

ex = pygame.image.load(r'EXIT.png')
ex_size = ex.get_rect().size

nana = pygame.image.load(r'Banan.png')
nana_size = nana.get_rect().size
nana.set_colorkey((255, 255, 255))


Boots = pygame.image.load(r'Boots.png')
Boots_size = Boots.get_rect().size
Boots.set_colorkey((52, 57, 40))


Potion = pygame.image.load(r'Potion.png')
Potion_size = Potion.get_rect().size
Potion.set_colorkey((112, 112, 112))
class shop:
    def __init__(self):
        self.xpos = 1500
        self.ypos = 400
        self.width = 75
        self.height = 75
        self.frameNum = 0
        self.RowNum = 0
        self.WynoAlive = False
        
        self.ticker = 0
    def interact(self, Px, Py, xoff, yoff, w, h):
        keys = pygame.key.get_pressed()
        if (self.ypos + self.height) + yoff >= Py and self.ypos + yoff <= Py + h and (self.xpos + self.width) + xoff >= Px and self.xpos + xoff <= Px + w:
            return True
        else:
            return False
    def store(self, inside, screen):
        self.WynoAlive = True
        WynoWidth = 320
        WynoHeight = 320
        Row = 0
        Frame = 0
        
        x = 0
        y = 0
        pos = (x, y)
        
        if inside == True: 

#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     pos = event.pos
#                 
                    
            if self.WynoAlive == True:
                self.ticker += 1
            if self.ticker % 50 == 0:
                    Frame += 1
                    self.ticker = 0
            if Frame > 8:
                    Frame = 0
            #print(self.ticker)
            print(Frame)
            screen.blit(Inside, (0,0))
            screen.blit(nana, (284, 225))
            screen.blit(Boots, (415, 220))
            screen.blit(Potion, (576, 215))
            screen.blit(wyno, (320, 500), (WynoWidth * Frame, Row * WynoHeight, WynoWidth, WynoHeight))
            screen.blit(ex, (25, 700))
            
            
    def draw(self, screen, xoff, yoff):
        screen.blit(outside, (self.xpos + xoff, self.ypos + yoff), (self.width*self.frameNum, self.RowNum * self.height, self.width, self.height))