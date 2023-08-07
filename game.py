import pygame
from random import randint as r
import time
pygame.init()

#display
display_w=1200
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
#
# while not rd:
#
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN and event.unicode in '0123456789':
#             msg += event.unicode
#
#
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_TAB:
#                 if len(msg)>0:
#                     if 2<=int(msg)<=40:
#                         rd=True
#                     else:
#                         bad=True
#                         sz+=6
#             if event.key==pygame.K_BACKSPACE:
#                 msg=msg[:-1]
#                 if sz>10:
#                     sz-=10
#     display.fill((0, 0, 0))
#     if not bad:
#         print_txt('press Tab чтобы подтвердить', 20, 200, size=20)
#     else:
#         print_txt('введите целое число от 2 до 40', 20, 200, size=sz)
#     print_txt('enter_n:', 20, 400)
#     print_txt(msg, x=200, y=400)
#     pygame.display.update()
#     clock.tick(60)
#
# n=int(msg)

n=5
#n=int(input('n='))

con=750/n
player_x=125+con/4
player_y=750-3*(con/4)
def move(key):

    global player_x,player_y,con,x_crd,y_crd
    if key==pygame.K_UP and player_y!=con/4:
        player_y-=con
        y_crd-=1
    elif key==pygame.K_DOWN and player_y!=750-3*(con/4):
        player_y+=con
        y_crd+=1
    elif key==pygame.K_RIGHT and player_x!=875-3*(con/4):
        player_x+=con
        x_crd+=1
    elif key==pygame.K_LEFT and player_x!=125+con/4:
        player_x-=con
        x_crd-=1


cells= [[tuple(r(0,255) for j in range(3)) for i in range(n)] for y in range(n)]
goal= [cells[r(0,n-1)][r(0,n-1)],cells[r(0,n-1)][r(0,n-1)],cells[r(0,n-1)][r(0,n-1)]]
cnt=[0,0,0]
while len(set(goal))!=3 or cells[0][n-1] in goal:
    goal = [cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)]]


x_crd=0
y_crd=n-1


def change_clrs():
    global cells,n
    for i in range(n):
        for j in range(n):
            cells[i][j]=tuple(r(0,255) for j in range(3))

tm1=None
dif=None
win = False
while True:
    if cnt==[1,1,1]:
        win=True
    if not win:
        current_clr=cells[x_crd][y_crd]
        if current_clr in goal:
            if tm1 is None:
                tm1=time.time()
            else:
                dif=time.time()-tm1
                if dif>=2:
                    cnt[goal.index(current_clr)] += 1
                    tm1=None
                    dif=None
        else:
            tm1=None
            dif=None
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    change_clrs()
            if event.type==pygame.KEYDOWN and event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]:
                # if current_clr in goal:
                #     if time.time()-tm1>=1:
                #         cnt[goal.index(current_clr)] += 1
                #     tm1=None
                move(event.key)


        pygame.draw.rect(display,(200,100,100),(125,0,750,750))

        keys=pygame.key.get_pressed()
        display.fill((0, 0, 0))

        for i in range(n):
            for j in range(n):
                pygame.draw.rect(display, cells[i][j],(125+i*con,0+j*con,con,con))
        pygame.draw.rect(display,(0,0,0),(player_x,player_y,con/2,con/2))

        pygame.draw.rect(display, goal[0], (900,250,40,40))
        print_txt(str(cnt[0])+"/3",950,255)
        pygame.draw.rect(display, goal[1], (900, 350, 40, 40))
        print_txt(str(cnt[1])+"/3", 950, 355)
        pygame.draw.rect(display, goal[2], (900, 450, 40, 40))
        print_txt(str(cnt[2])+"/3", 950, 455)
        if dif!=None:
            print_txt(str(round(dif,4)), 950, 555)
        #pygame.draw.rect(display, current_clr, (950, 550, 60, 60))
    else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((0, 0, 0))
        print_txt('U WIN', 100, 100, size=50)
    pygame.display.update()
    clock.tick(60)

