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
display.fill((0,0,0))
clock=pygame.time.Clock()



#n=int(input('n='))
n=5
con=750/n
player_x=125+con/4
player_y=750-3*(con/4)
def move(key):
    global player_x,player_y,con
    if key==pygame.K_UP and player_y!=con/4:
        player_y-=con
    elif key==pygame.K_DOWN and player_y!=750-3*(con/4):
        player_y+=con
    elif key==pygame.K_RIGHT and player_x!=875-3*(con/4):
        player_x+=con
    elif key==pygame.K_LEFT and player_x!=125+con/4:
        player_x-=con

cells= [[tuple(r(0,255) for j in range(3)) for i in range(n)] for y in range(n)]




def change_clrs():
    global cells,n
    for i in range(n):
        for j in range(n):
            cells[i][j]=tuple(r(0,255) for j in range(3))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                change_clrs()
        if event.type==pygame.KEYDOWN and event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]:
            move(event.key)
            change_clrs()
    pygame.draw.rect(display,(200,100,100),(125,0,750,750))

    keys=pygame.key.get_pressed()
    display.fill((0, 0, 0))
    for i in range(n):
        for j in range(n):
            pygame.draw.rect(display, cells[i][j],(125+i*con,0+j*con,con,con))
    pygame.draw.rect(display,(0,0,0),(player_x,player_y,con/2,con/2))

    pygame.display.update()
    clock.tick(60)

