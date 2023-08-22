import pygame
from random import randint as r
import time

###всё это для создания окна+дисплея
pygame.init()
display_w=1200
display_h=750
display=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Game1')
icon=pygame.image.load('ico1.png')
cur=pygame.image.load('cur1.png')
pygame.display.set_icon(icon)
display.fill((0,0,0))
clock=pygame.time.Clock()   #это просто для обновления дисплея и контроля фпс крч

def print_txt(txt,x,y,size=30,clr=(255,255,255)):  #это чтобы выводить текст на дисплей
    font_type=pygame.font.Font('better-vcr_0.ttf',size)
    text=font_type.render(txt,True,clr)
    display.blit(text,(x,y))

### вот это всё чтобы выбрать модификаторы
rd=False
def mod1(a,b):
    return (a-30)**2+(b-130)**2<=15**2
def mod2(a,b):
    return (a-30)**2+(b-180)**2<=15**2

def mod1_txt(a,b):
    return (10<=a<=333) and (113<=b<=143)
def mod2_txt(a,b):
    return (10<=a<=293) and (163<=b<=193)
pygame.mouse.set_visible(False)
dfclt=[False,False]#move_cntr,dead cells
while not rd:
    cur_x, cur_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rd=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if mod1(cur_x,cur_y):
                    if dfclt[0]==True:
                        dfclt[0]=False
                    else:
                        dfclt[0]=True
                elif mod2(cur_x,cur_y):
                    if dfclt[1]==True:
                        dfclt[1]=False
                    else:
                        dfclt[1]=True
    display.fill((0, 0, 0))
    print_txt('Mods:', 40, 40)
    print_txt('Press Space to start', 40, 600)
    if dfclt[0]:
        clr1=(0,255,0)
    else:
        clr1 = (255, 0, 0)
    if dfclt[1]:
        clr2=(0,255,0)
    else:
        clr2 = (255, 0, 0)
    if mod1_txt(cur_x,cur_y):
        print_txt('mod1_description', x=500, y=213)
    elif mod2_txt(cur_x,cur_y):
        print_txt('mod2_description', x=500, y=213)
    pygame.draw.circle(display,clr1,(30,130),15)
    pygame.draw.circle(display, clr2, (30, 180), 15)
    if pygame.mouse.get_focused():
        display.blit(cur,(cur_x-25,cur_y-35))
    print_txt('move_counter',x=60,y=113)
    print_txt('dead_cells', x=60, y=163)
    pygame.display.update()
    clock.tick(60)




clrs=[(000,255,255),(000,000,255),(255,000,255),(000,255,000),(000,128,000),(128,000,128),
      (255,000,000),(255,255,000),(255,203,219),(0, 250, 154),
      (127, 255, 212),(165, 42, 42),(128, 128, 128),(47, 79, 79),(188, 143, 143),(210, 105, 30),
      (0, 0, 128),(218, 165, 32)]


###тут задаю основные переменные
n=100  #размер поля
cells= [[clrs[r(0,len(clrs)-1)] for i in range(n)] for y in range(n)] #массив в котором хранятся цвета для каждой из клеток
if dfclt[0]: #это чиселки которые будут в каждой из клеток
    nums=[ [r(-5,5) for i in range(n)] for j in range(n) ]
    nums[0][n-1]=None
    moves=20
if dfclt[1]: #тут храним инфу мёртвая ли клетка
    dead=[[False for i in range(n)] for j in range(n)]

goal= []  #тут придумываю 3 цвета которые нужно будет собрать
cnt=[0,0,0] #счётчик собранных цветов
pwr=3#кол-во возможных смен цветов
while len(goal)!=3:
    x=cells[r(0,n-1)][r(0,n-1)]
    if x!=cells[0][n-1] and x not in goal:
        goal.append(x)


msg=''#причина проигрыша
con=750/n #размер стороны квадрата
player_x=125+con/4 #координаты игрока в пикселях
player_y=750-3*(con/4)
x_crd=0 #координаты игрока в СО связанной с клетками типа 1-й ряд 3-й столбец
y_crd=n-1
tm1=None #
dif=None #это для подсчёта времени стояния на текущей клетке
win_st = False #это чтобы активировать функции окончания игры
st=time.time() #время начала игры
time_lim=20
nums_g={i:pygame.font.Font('better-vcr_0.ttf',int(con/2)).render(str(i),True,(255,255,255)) for i in range(-5,6)}





def print_num(num,x,y):  #это чтобы выводить чиселки на дисплей
    global nums_g
    display.blit(nums_g[num],(x,y))

def move(key): #эта ответственна за передвижки она меняет координаты
    global player_x,player_y,con,x_crd,y_crd,moves,dfclt
    if dfclt[0]:
        moves-=1
    if key==pygame.K_UP and player_y!=con/4:
        if dfclt[1]:
            dead[x_crd][y_crd]=True
        player_y-=con
        y_crd-=1
    elif key==pygame.K_DOWN and player_y!=750-3*(con/4):
        if dfclt[1]:
            dead[x_crd][y_crd]=True
        player_y+=con
        y_crd+=1
    elif key==pygame.K_RIGHT and player_x!=875-3*(con/4):
        if dfclt[1]:
            dead[x_crd][y_crd]=True
        player_x+=con
        x_crd+=1
    elif key==pygame.K_LEFT and player_x!=125+con/4:
        if dfclt[1]:
            dead[x_crd][y_crd]=True
        player_x-=con
        x_crd-=1



def restart(): #при рестарте заново инициализирует все переменные (да так нужно)
    global cells,goal,cnt,player_y,player_x,x_crd,y_crd,tm1,dif,win_st,st,n,msg,dfclt,nums,moves,dead,pwr
    pwr=3
    cells= [[clrs[r(0,len(clrs)-1)] for i in range(n)] for y in range(n)]
    if dfclt[0]:
        moves = 20
        nums = [[r(-5, 5) for i in range(n)] for j in range(n)]
        nums[0][n - 1] = None
    if dfclt[1]:
        if dfclt[1]:
            dead = [[False for i in range(n)] for j in range(n)]
    cnt = [0, 0, 0]
    goal=[]
    while len(goal) != 3:
        x = cells[r(0, n - 1)][r(0, n - 1)]
        if x != cells[0][n - 1] and x not in goal:
            goal.append(x)
    player_x = 125 + con / 4
    player_y = 750 - 3 * (con / 4)
    x_crd = 0
    y_crd = n - 1
    tm1 = None
    dif = None
    win_st = False
    st = time.time()


def change_clrs(): #меняет все цвета (см. строки 153-155)
    global goal,cells,time_lim,nums
    global cells,n
    if dfclt[0]:
        nums = [[r(-5, 5) for i in range(n)] for j in range(n)]
        nums[0][n - 1] = None
    for i in range(n):
        for j in range(n):
            cells[i][j]=clrs[r(0,len(clrs)-1)]
    goal = []  # тут придумываю 3 цвета которые нужно будет собрать
    while len(goal) != 3:
        x = cells[r(0, n - 1)][r(0, n - 1)]
        if x != cells[0][n - 1] and x not in goal:
            goal.append(x)


def game(): #НОУ КОММЕНТО
    global win_st,dif,tm1,goal,cnt,cells,display,clock,time_lim,moves,msg,nums,pwr
    while True: #бесконечный(нет) цикл обработки событий
        if cnt==[2,2,2]: #проверяем а вдрг уже собрал всё
            win_st=True
        if dfclt[0]:
            if moves<=0 and cnt!=[2,2,2]:  #проверяем а вдруг проиграл(кончились ходы)
                lose('out of moves')
        if dfclt[1]: #проверяем а вдруг проиграл(встал на мёртвую клетку)
            if dead[x_crd][y_crd]:
                lose('dont step on dead cells')
        if not win_st:#если ты НЕ ВЫИГРАЛ
            current_clr=cells[x_crd][y_crd] #сука это блядь интуитивно понятно разрази тебя варда но я напишу что ЭТО ЦВЕТ КЛЕТКИ НА КОТОРОЙ СТОИТ ИГРОК
            if dfclt[0]:
                plus=nums[x_crd][y_crd]
                if plus!=None:
                    moves+=plus
                    nums[x_crd][y_crd]=None
            if current_clr in goal: #если ты стоишь на цвете что нужно собрать
                if tm1 is None:
                    tm1=time.time() #время входа на клетку
                else:
                    dif=time.time()-tm1 # разница между текущим временем и временем входа на клетку чтоб понять скок стоишь уже
                    if dif>=2: #если стоишь достаточно то +респект
                        cnt[goal.index(current_clr)] += 1

                        y=[r(0,n-1),r(0,n-1)]
                        while y==[x_crd,y_crd]:
                            y = [r(0, n - 1), r(0, n - 1)]
                        nxt_clr=cells[y[0]][y[1]]
                        cells[y[0]][y[1]]=current_clr
                        cells[x_crd][y_crd]=nxt_clr
                        tm1=None
                        dif=None
            else:#если встал на ненужный цвет все счётчики времени сбросить
                tm1=None
                dif=None

            for event in pygame.event.get(): #перебор ВСЕХ событий в приложении
                if event.type==pygame.QUIT:#ноу коменто
                    pygame.quit()
                    quit()

                if event.type==pygame.KEYDOWN and event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]:#ноу коменто
                    move(event.key)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pwr>=1:
                            pwr-=1
                            change_clrs()
            display.fill((0, 0, 0))#покраска дисплея
            pygame.draw.rect(display,(200,100,100),(125,0,750,750)) #отрисовка игрового поля покачто не роляет но потом на месте заливки будет рамка красивая

            if dfclt[0]:
                for i in range(n):  # отрисовка квадратиков цветовых
                    for j in range(n):
                        pygame.draw.rect(display, cells[i][j], (125 + i * con, 0 + j * con, con, con))
                        if dfclt[1]:
                            if dead[i][j]==True:
                                print_txt('X',x=125 + i * con,y=0 + j * con,size=int(con/2))
                                continue
                        if nums[i][j]!=None:
                            print_num(num=nums[i][j],x=125 + i * con,y=0 + j * con)
            else:
                for i in range(n):#отрисовка квадратиков цветовых
                    for j in range(n):
                        pygame.draw.rect(display, cells[i][j],(125+i*con,0+j*con,con,con))
                        if dfclt[1]:
                            if dead[i][j]==True:
                                print_txt('X',x=125 + i * con,y=0 + j * con,size=int(con/2))
            pygame.draw.rect(display,(0,0,0),(player_x,player_y,con/2,con/2)) #отрисовка игрока

            ### отрисовка всей панельки справа
            if dfclt[0]:
                print_txt('moves:'+str(moves), 900, 20)
            pygame.draw.rect(display, goal[0], (900,250,40,40))
            print_txt(str(cnt[0])+"/2",950,255)
            pygame.draw.rect(display, goal[1], (900, 350, 40, 40))
            print_txt(str(cnt[1])+"/2", 950, 355)
            pygame.draw.rect(display, goal[2], (900, 450, 40, 40))
            print_txt(str(cnt[2])+"/2", 950, 455)
            print_txt('game time:', 900, 85)
            total_tm=round(time_lim-(time.time()-st),3)
            print_txt("pwr:", 900, 185)
            print_txt(str(pwr)+"/3", 1000, 185)

            if total_tm<=0:#проверка не вышло ли время
                lose('(out of time)')
            else:
                print_txt(str(total_tm), 900, 125)

            if dif:#отрисовка времени на текущей клетке
                print_txt(str(round(dif,3)), 950, 555)
            #pygame.draw.rect(display, current_clr, (950, 550, 60, 60))
        else: #если выиграл)))
            win()
        pygame.display.update()#крч просто смена кадров
        clock.tick(60)


def lose(msg): #активируется при проигрыше
    global clock,display
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    game()
        display.fill((255, 0, 0))
        print_txt('U LOSE', 100, 100, size=50)
        print_txt(str(msg), 100, 200, size=50)
        print_txt('press Space to restart', 100, 300, size=40)
        pygame.display.update()
        clock.tick(60)


def win(): #активируется при выигрыше
    global clock, display
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    game()
        display.fill((0, 255, 0))
        print_txt('U WON', 100, 100, size=50)
        print_txt('press Space to restart', 100, 300, size=40)
        pygame.display.update()
        clock.tick(60)


game() #запуск игры
