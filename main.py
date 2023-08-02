import pygame
from random import randint as r
pygame.init()

display_w=800
display_h=600

display=pygame.display.set_mode((display_w,display_h))


pygame.display.set_caption('Game1')
icon=pygame.image.load('ico1.png')
pygame.display.set_icon(icon)

usr_w=100
usr_h=100
usr_x=display_w/2-100
usr_y=display_h/2

cactus_w=30
cactus_h=80
cactus_x=display_w
cactus_y=display_h/2+20


class Cactus:
    def __init__(self,x,y,w,h,speed):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=speed
    def move(self):
        if self.x >= -self.w:
            pygame.draw.rect(display, (100, 25, 90), (self.x,self.y,self.w,self.h))
            self.x -= self.speed
        else:
            self.x = display_w+100+r(-100,100)
            dif=r(-20,80)
            self.h=80+dif
            self.y=display_h/2+usr_h-self.h

clock=pygame.time.Clock()

make_jump=False
jump_cnt=30


def run_game():
    global make_jump
    game=True
    cactuses=[]
    create_cactuses(cactuses)
    land=pygame.image.load('land.png')
    sun=pygame.image.load('sun.png')
    while game:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump=True
        if make_jump:
            jump()
        display.fill((255, 100, 255))
        draw_cactuses(cactuses)
        pygame.draw.rect(display, (255, 255, 255), (usr_x, usr_y, usr_w, usr_h))
        display.blit(land,(0,400))
        display.blit(sun,(0,0))
        pygame.display.update()
        clock.tick(60)

def jump():
    global usr_y,make_jump,jump_cnt
    if jump_cnt>=-30:
        usr_y-=jump_cnt/2
        jump_cnt-=1
    else:
        jump_cnt=30
        make_jump=False
def create_cactuses(arr):
    arr.append(Cactus(display_w,display_h/2+20,30,80,4))
    arr.append(Cactus(display_w+300,display_h/2+20,30,80,4))
    arr.append(Cactus(display_w+100,display_h/2+20,30,80,4))

def draw_cactuses(arr):
    for cactus in arr:
        cactus.move()
run_game()
