import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

ScreenWidth = 1100
ScreenHeight = 750

canvas = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Game Board")
running = True

class Bed(pygame.sprite.Sprite):
    def __init__(this):
        super(Bed, this).__init__()
        this.surf = pygame.Surface((50,50))
        this.surf.fill((255,0,0))
        this.rect = this.surf.get_rect(center=(550, 375))

class Wall:
    def __init__(this,coords):
        super(Wall, this).__init__()
        this.surf = pygame.Surface((50,50))
        this.surf.fill((105, 56, 3))
        this.rect = this.surf.get_rect(center=(coords))

class Pillow:
    def __init__(this):
        super(Pillow, this).__init__()
        this.surf = pygame.Surface((30,15))
        this.surf.fill((255,255,255))
        this.rect = this.surf.get_rect(center=(550,360))

class Piggy:
    x=1
class Stone:
    x=1
class Wood:
    x=1

grassColor = (50,200,50)
canvas.fill(grassColor)
spriteList = []
bed = Bed()
spriteList.append(bed)
pillow = Pillow()
spriteList.append(pillow)
wall = Wall((500,375))
wall2 = Wall((600,375))
spriteList.append(wall)
spriteList.append(wall2)




while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
            
    for item in spriteList:
        canvas.blit(item.surf,item.rect)
    pygame.display.flip()
