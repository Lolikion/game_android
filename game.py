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

def print_txt(txt,x,y,size=30,clr=(255,255,255)):
    font_type=pygame.font.Font('better-vcr_0.ttf',size)
    text=font_type.render(txt,True,clr)
    display.blit(text,(x,y))
input_state=False
rd=False
msg = ''
bad=False
sz=10
while not rd:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.unicode in '0123456789':
            msg += event.unicode


        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if len(msg)>0:
                    if 2<=int(msg)<=40:
                        rd=True
                    else:
                        bad=True
                        sz+=6
            if event.key==pygame.K_BACKSPACE:
                msg=msg[:-1]
                if sz>10:
                    sz-=10
    display.fill((0, 0, 0))
    if not bad:
        print_txt('press Tab чтобы подтвердить', 20, 200, size=20)
    else:
        print_txt('введите целое число от 2 до 40', 20, 200, size=sz)
    print_txt('enter_n:', 20, 400)
    print_txt(msg, x=200, y=400)
    pygame.display.update()
    clock.tick(60)

n=int(msg)


#n=int(input('n='))

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

    pygame.draw.rect(display,(200,100,100),(125,0,750,750))

    keys=pygame.key.get_pressed()
    display.fill((0, 0, 0))

    for i in range(n):
        for j in range(n):
            pygame.draw.rect(display, cells[i][j],(125+i*con,0+j*con,con,con))
    pygame.draw.rect(display,(0,0,0),(player_x,player_y,con/2,con/2))

    pygame.display.update()
    clock.tick(60)

