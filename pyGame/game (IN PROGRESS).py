import pygame
import random
import time as clock
import math

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
    K_RIGHT,
    K_SPACE,
    K_k
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

birdImageRight = pygame.image.load('birdRight.png')
birdImageRight = pygame.transform.scale(birdImageRight,(50,50))
birdImageRight = birdImageRight.convert_alpha()

birdImageLeft = pygame.image.load('birdLeft.png')
birdImageLeft = pygame.transform.scale(birdImageLeft,(50,50))
birdImageLeft = birdImageLeft.convert_alpha()

treeImage = pygame.image.load('tree.png')
treeImage = pygame.transform.scale(treeImage,(150,150))
treeImage = treeImage.convert_alpha()

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
        self.spaceCheck = False
    def pigCollide(self):
        self.health-=5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.spaceCheck = False
        self.x = 600
        self.y = 375
        self.health = 20
        self.wood = 0
        self.woodActual = 0
        self.imageRight = birdImageRight
        self.imageLeft = birdImageLeft
        self.image = self.imageRight
        self.center = (self.x,self.y)
        self.rect = self.image.get_rect(center = self.center)
        self.surf = self.image
        self.lastTime = 0
        self.hit = False
        self.axeLevel = 1
        self.pickLevel = 0
        self.swordLevel = 1
    def upgradeAxe(self):
        self.axeLevel+=1
    def upgradePick(self):
        self.pickLevel+=1
    def upgradeSword(self):
        self.swordLevel+=1
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
        self.image = self.imageRight
        self.rect = self.image.get_rect(center = self.center)
        self.surf = self.image
        self.x+=0.45
    def moveLeft(self):
        self.image = self.imageLeft
        self.rect = self.image.get_rect(center = self.center)
        self.surf = self.image
        self.x-=0.45
    def moveUp(self):
        self.y-=0.45
    def moveDown(self):
        self.y+=0.45
    def woodAdd(self):
        self.wood+=1
    def woodDel(self):
        self.wood-=1
    def pigCollide(self):
        self.hit = True
        if (math.floor(clock.time())-self.lastTime>0):
            self.health -= 2
            self.lastTime = math.floor(clock.time())+1
            self.hit = False


class Wall:
    x=1

class Pillow:
    def __init__(self):
        super(Pillow, self).__init__()
        self.surf = pygame.Surface((30,15))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(550,360))
        self.spaceCheck = False

class Piggy(pygame.sprite.Sprite):
    def __init__(self,coords):
        super(Piggy, self).__init__()
        self.x = coords[0]
        self.y = coords[1]
        self.image = pigImage
        self.center = (self.x,self.y)
        self.rect = self.image.get_rect(center = self.center)
        self.surf = self.image
        self.spaceCheck = True
        self.name = 'piggy'
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
class Wood(pygame.sprite.Sprite):
    def __init__(self,coords):
        pygame.sprite.Sprite.__init__(self)
        self.center = coords
        self.x = coords[0]
        self.y = coords[1]
        self.image = treeImage
        self.surf = self.image
        self.rect = self.surf.get_rect(center = self.center)
        self.spaceCheck = True
        self.name = "tree"

grassColor = (50,200,50)
canvas.fill(grassColor)
spriteList = []
bed = Bed()
spriteList.append(bed)
pillow = Pillow()
spriteList.append(pillow)
tree1 = Wood((random.randint(500,1030),random.randint(50,300)))
spriteList.append(tree1)
tree2 = Wood((random.randint(50,430),random.randint(50,300)))
spriteList.append(tree2)
tree3 = Wood((random.randint(50,430),random.randint(350,680)))
spriteList.append(tree3)
tree4 = Wood((random.randint(500,1030),random.randint(375,680)))
spriteList.append(tree4)
player = Player()
spriteList.append(player)

night1 = None

prevMove = None

while running:
    player.woodActual = player.wood/500/player.axeLevel
    bedHealth = font.render("Bed Health: "+str(bed.health), True, WHITE, grassColor)
    playerHealth = font.render("Player Health: "+str(player.health), True, WHITE, grassColor)
    woodInv = font.render("Wood: "+str(int(player.woodActual)), True, WHITE, grassColor)
    playerHealthRect = playerHealth.get_rect()
    bedHealthRect = bedHealth.get_rect()
    woodInvRect = woodInv.get_rect()
    bedHealthRect.center = ((55,10))
    playerHealthRect.center = ((60,27))
    woodInvRect.center = ((30,43))

    canvas.fill(grassColor)

    if ((time/5)%2==0):
        grassColor = (50,200,50)
    elif ((time/5)==1.00 and night1!=False):
        night1 = True
        grassColor = (0,74,0)
    keys = pygame.key.get_pressed()
    pygame.key.set_repeat(500,500)
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
    if keys[K_SPACE]:
        for sprites in spriteList:
            if (sprites.spaceCheck==True):
                if ((abs(sprites.x - player.x)<80) and (abs(sprites.y - player.y)<80)):
                    if sprites.name == 'tree':
                        print(pygame.time.get_ticks())
                        player.woodAdd()
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
            birdCollidePig = item.rect.colliderect(player.rect)
            if birdCollidePig:
                player.pigCollide()
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
                pigCollideBed = item.rect.colliderect(bed.rect)
                if pigCollideBed:
                    bed.pigCollide()

        time = int((clock.time()-initialTime))
        canvas.blit(item.surf,item.rect)
    
    canvas.blit(bedHealth, bedHealthRect)
    canvas.blit(playerHealth, playerHealthRect)
    canvas.blit(woodInv, woodInvRect)

    pygame.display.flip()
