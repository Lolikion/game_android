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
pygame.display.set_icon(icon)
display.fill((0,0,0))
clock=pygame.time.Clock()   #это просто для обновления дисплея и контроля фпс крч


### вот это всё чтобы задавать размер поля но я его закоментил нахуй пока что нет нужды можеш расскоментить и посмотреть
# input_state=False
# rd=False
# msg = ''
# bad=False
# sz=10
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
#n=int(input('n='))


###тут задаю основные переменные
n=4   #размер поля
cells= [[tuple(r(0,255) for j in range(3)) for i in range(n)] for y in range(n)] #массив в котором хранятся цвета для каждой из клеток
goal= [cells[r(0,n-1)][r(0,n-1)],cells[r(0,n-1)][r(0,n-1)],cells[r(0,n-1)][r(0,n-1)]]  #тут придумываю 3 цвета которые нужно будет собрать
cnt=[0,0,0] #счётчик собранных цветов
while len(set(goal))!=3 or cells[0][n-1] in goal: #костыль чтобы было ВОЗМОЖНО найти нужнеы цвета
    goal = [cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)]]
con=750/n #размер стороны квадрата
player_x=125+con/4 #координаты игрока в пикселях
player_y=750-3*(con/4)
x_crd=0 #координаты игрока в СО связанной с клетками типа 1-й ряд 3-й столбец
y_crd=n-1
tm1=None #
dif=None #это для подсчёта времени стояния на текущей клетке
win_st = False #это чтобы активировать функции окончания игры
lose_st=False
st=time.time() #время начала игры
time_lim=20


def print_txt(txt,x,y,size=30,clr=(255,255,255)):  #это чтобы выводить текст на дисплей
    font_type=pygame.font.Font('better-vcr_0.ttf',size)
    text=font_type.render(txt,True,clr)
    display.blit(text,(x,y))


def move(key): #эта ответственна за передвижки она меняет координаты
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


def restart(): #при рестарте заново инициализирует все переменные (да так нужно)
    global cells,goal,cnt,player_y,player_x,x_crd,y_crd,tm1,dif,win_st,lose_st,st,n
    cells = [[tuple(r(0, 255) for j in range(3)) for i in range(n)] for y in range(n)]
    goal = [cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)]]
    cnt = [0, 0, 0]
    while len(set(goal)) != 3 or cells[0][n - 1] in goal:
        goal = [cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)], cells[r(0, n - 1)][r(0, n - 1)]]
    player_x = 125 + con / 4
    player_y = 750 - 3 * (con / 4)
    x_crd = 0
    y_crd = n - 1
    tm1 = None
    dif = None
    win_st = False
    lose_st = False
    st = time.time()


def change_clrs(): #меняет все цвета (см. строки 153-155)
    global cells,n
    for i in range(n):
        for j in range(n):
            cells[i][j]=tuple(r(0,255) for j in range(3))


def game(): #НОУ КОММЕНТО
    global lose_st,win_st,dif,tm1,goal,cnt,cells,display,clock,time_lim
    while True: #бесконечный(нет) цикл обработки событий
        if cnt==[2,2,2]: #проверяем а вдрг уже собрал всё
            win_st=True
        if lose_st==True: #проверяем а вдруг проиграл
            lose()
        else: #если ты НЕ ПРОИГРАЛ
            if win_st==False:#если ты НЕ ВЫИГРАЛ
                current_clr=cells[x_crd][y_crd] #сука это блядь интуитивно понятно разрази тебя варда но я напишу что ЭТО ЦВЕТ КЛЕТКИ НА КОТОРОЙ СТОИТ ИГРОК
                if current_clr in goal: #если ты стоишь на цвете что нужно собрать
                    if tm1 is None:
                        tm1=time.time() #время входа на клетку
                    else:
                        dif=time.time()-tm1 # разница между текущим временем и временем входа на клетку чтоб понять скок стоишь уже
                        if dif>=2: #если стоишь достаточно то +респект
                            cnt[goal.index(current_clr)] += 1
                            tm1=None
                            dif=None
                else:#если встал на ненужный цвет все счётчики времени сбросить
                    tm1=None
                    dif=None

                for event in pygame.event.get(): #перебор ВСЕХ событий в приложении
                    if event.type==pygame.QUIT:#ноу коменто
                        pygame.quit()
                        quit()
                    # if event.type==pygame.KEYDOWN:
                    #     if event.key==pygame.K_SPACE:
                    #         change_clrs()
                    if event.type==pygame.KEYDOWN and event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]:#ноу коменто
                        move(event.key)

                display.fill((0, 0, 0))#покраска дисплея
                pygame.draw.rect(display,(200,100,100),(125,0,750,750)) #отрисовка игрового поля покачто не роляет но потом на месте заливки будет рамка красивая


                for i in range(n):#отрисовка квадратиков цветовых
                    for j in range(n):
                        pygame.draw.rect(display, cells[i][j],(125+i*con,0+j*con,con,con))
                pygame.draw.rect(display,(0,0,0),(player_x,player_y,con/2,con/2)) #отрисовка игрока

                ### отрисовка всей панельки справа
                pygame.draw.rect(display, goal[0], (900,250,40,40))
                print_txt(str(cnt[0])+"/2",950,255)
                pygame.draw.rect(display, goal[1], (900, 350, 40, 40))
                print_txt(str(cnt[1])+"/2", 950, 355)
                pygame.draw.rect(display, goal[2], (900, 450, 40, 40))
                print_txt(str(cnt[2])+"/2", 950, 455)
                print_txt('game time:', 900, 55)
                total_tm=round(time_lim-(time.time()-st),4)

                if total_tm<=0:#проверка не вышло ли время
                    lose_st=True
                else:
                    print_txt(str(total_tm), 900, 95)

                if dif!=None:#отрисовка времени на текущей клетке
                    print_txt(str(round(dif,4)), 950, 555)
                #pygame.draw.rect(display, current_clr, (950, 550, 60, 60))
            else: #если выиграл)))
                win()
        pygame.display.update()#крч просто смена кадров
        clock.tick(60)


def lose(): #активируется при проигрыше
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
        print_txt('U WIN', 100, 100, size=50)
        print_txt('press Space to restart', 100, 300, size=40)
        pygame.display.update()
        clock.tick(60)


game() #запуск игры
