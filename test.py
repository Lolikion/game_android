import pygame
from random import randint as r

pygame.init()

#display
display_w=1000
display_h=750
display=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Game1')
icon=pygame.image.load('ico1.png')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()


n=int(input('n='))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(display,(200,100,100),(125,0,750,750))
    con=750/n
    for i in range(n):
        for j in range(n):
            pygame.draw.rect(display, (r(0,255),r(0,255),r(0,255)),(125+i*con,0+j*con,con,con))
    pygame.display.update()
    clock.tick(60)

