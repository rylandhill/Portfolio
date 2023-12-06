import pygame
import random
import time as clock

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_UP,
    K_LEFT,
    K_DOWN,
    K_RIGHT
)

pygame.init()

BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

time = 0
initialTime = clock.time()

screenWidth = 1100
screenHeight = 750
defaultImageSize = (50,50)

font = pygame.font.Font(None,20)

canvas = pygame.display.set_mode((screenWidth,screenHeight))

pigImage = pygame.image.load('bad_piggy.png')
pigImage = pygame.transform.scale(pigImage,(70,70))
pigImage = pigImage.convert_alpha()

birdImage = pygame.image.load('bird.png')
birdImage = pygame.transform.scale(birdImage,(50,50))
birdImage = birdImage.convert_alpha()

pygame.display.set_caption("Game Board")
running = True

class Bed(pygame.sprite.Sprite):
    def __init__(self):
        super(Bed, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255,0,0))
        self.center = (550,375)
        self.rect = self.surf.get_rect(center=self.center)
        self.health = 100
    def pigCollide(self):
        self.health-=5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.x = 600
        self.y = 375
        self.health = 20
        self.image = birdImage
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.surf = self.image
    def updateImage(self):
        if (self.x>=1050):
            self.x = 1050
        if (self.x<=50):
            self.x = 50
        if (self.y>=700):
            self.y = 700
        if (self.y<=50):
            self.y = 50
        self.rect = self.image.get_rect(center = (self.x,self.y))
    def moveRight(self):
        self.x+=0.8
    def moveLeft(self):
        self.x-=0.8
    def moveUp(self):
        self.y-=0.8
    def moveDown(self):
        self.y+=0.8


class Wall:
    x=1

class Pillow:
    def __init__(self):
        super(Pillow, self).__init__()
        self.surf = pygame.Surface((30,15))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(550,360))

class Piggy(pygame.sprite.Sprite):
    def __init__(self,coords):
        super(Piggy, self).__init__()
        self.x = coords[0]
        self.y = coords[1]
        self.image = pigImage
        self.rect = self.image.get_rect(center = coords)
        self.surf = self.image
    def updateImage(self):
        self.rect = self.image.get_rect(center = (self.x,self.y))
    def moveRight(self):
        self.x+=10
    def moveLeft(self):
        self.x-=10
    def moveUp(self):
        self.y-=10
    def moveDown(self):
        self.y+=10

class Stone:
    x=1
class Wood:
    def __init__(self,coords):
        super(Wood, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((105, 56, 3))
        self.rect = self.surf.get_rect(center=(coords))

grassColor = (50,200,50)
canvas.fill(grassColor)
spriteList = []
bed = Bed()
spriteList.append(bed)
pillow = Pillow()
spriteList.append(pillow)
tree1 = Wood((random.randint(500,1050),random.randint(50,325)))
spriteList.append(tree1)
tree2 = Wood((random.randint(50,450),random.randint(50,350)))
spriteList.append(tree2)
tree3 = Wood((random.randint(50,450),random.randint(350,700)))
spriteList.append(tree3)
tree4 = Wood((random.randint(500,1050),random.randint(375,700)))
spriteList.append(tree4)
player = Player()
spriteList.append(player)

night1 = None

prevMove = None

while running:
    text = font.render("Bed Health: "+str(bed.health), True, WHITE, grassColor)
    textRect = text.get_rect()
    textRect.center = ((55,10))

    canvas.fill(grassColor)

    if ((time/5)%2==0):
        grassColor = (50,200,50)
    elif ((time/5)==1.00 and night1!=False):
        night1 = True
        grassColor = (0,74,0)
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    if keys[K_w] or keys[K_UP]:
        player.moveUp()
    if keys[K_a] or keys[K_LEFT]:
        player.moveLeft()
    if keys[K_s] or keys[K_DOWN]:
        player.moveDown()
    if keys[K_d] or keys[K_RIGHT]:
        player.moveRight()
    player.updateImage()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

    if (night1):
        spriteList.append(Piggy((random.randint(30,screenWidth-30),30)))
        spriteList.append(Piggy((random.randint(30,screenWidth-30),720)))
        spriteList.append(Piggy((30,random.randint(30,screenHeight-30))))
        spriteList.append(Piggy((screenWidth-30,random.randint(30,screenHeight-30))))
        night1 = False
    
    if (prevMove!=time):
        movement = True
    else:
        movement = False
    
    for item in spriteList:
        if (type(item)==type(Piggy((100000,10000)))):
            if movement:
                if(item.x>565):
                    item.moveLeft()
                if(item.x<520):
                    item.moveRight()
                if(item.y<375):
                    item.moveDown()
                if(item.y>375):
                    item.moveUp()
                item.updateImage()
                prevMove = time
                collide = item.rect.collidepoint(bed.center)
                if collide:
                    bed.pigCollide()

        time = int((clock.time()-initialTime))
        canvas.blit(item.surf,item.rect)
    
    canvas.blit(text, textRect)

    pygame.display.flip()
