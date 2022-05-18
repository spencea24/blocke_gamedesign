# Ava Spence
# LEARNING OBJECTIVE:
    # draw circles + rectangles
    # use keys to move objects
    # use dictionaries
# GAME OBJECTIVE:
    # rectangle runs from circle-- if they collide, the circle consumes square + becomes larger, and new rectangle appears on screen 

import os, random, time, pygame, math, datetime
from platform import java_ver
from turtle import screensize
os.system('cls')
name=input("What's your name? \nEnter name: ")
# Initialize pygame
pygame.init()

# Declare constants, variables, lists, dictionaries, objects
# Screen size
WIDTH = 700
HEIGHT = 700
xs = 50
ys = 250
wb = 30
hb = 30
MAIN = True
INST = False
SETT = False
LEV_I = False
LEV_II = False
LEV_III = False
SCORE = False
SC_SIZE = False
BG_COLOR = False
SPRITE = False
ON_OFF = False
f_SEET=False
xm = 0
ym = 0
sc = False

# List of messages
MenuList = ['Instructions','Settings', 'Level I', 'Level II', 'Level III', 'Score', 'Exit']
SettingList = ['Screen Size', 'Background Color', 'Icon', '']
SC_sizeList=['1000 x 1000', '800 x 800', '600 x 600']
check = True    # this is for the while loop

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Circle Eats Square')

# Define colors
colors= {'black':[0,0,0], 'grey':[128,128,128], 'white':[255,255,255], 'red':[255,0,0], 'orange':[255,128,0], 'yellow':[255,230,0], 'green':[0,204,0], 'blue':[0, 128, 255], 'purple':[153,51,255], 'pink':[255,102,178]}
# Get colors
background = colors.get('white')
randColor = ''
cr_color = ('aqua') #colors.get('aqua')
sq_color = ('pink') #colors.get('pink')

# Create different type
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('arial', 40)
INST_FNT=pygame.font.SysFont('arial', 30)

square = pygame.Rect(xs,ys,wb,hb)
# Create title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, 'red')
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
# this is a function that uses a parameter
def MainMenu(MList):
    txty=243
    square.y=250
    for i in range(len(MList)):
        message = MList[i]
        text = INST_FNT.render(message,1,'black')
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen, 'orange', square)
        square.y += 50
        txty += 50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print('in instr')
    myFile = open('ces\menu\instructions.txt', 'r')
    yi = 200
    stuff = myFile.readlines()
    print(stuff)
    for line in stuff:
        print(line)
        text = INST_FNT.render(line, 1, 'black')
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 50
    myFile.close()
def keepScore(score):
    date = datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score) + " " + name + " " + date.strftime('%m/%d/%Y' + '\n')
    # Open a file and write stuff in it.... when you write it erases the previous
    myFile = open('misc\sce.txt', 'w')
    myFile.write(scoreLine)
    myFile.close
def changeScreenSize(xm, ym):
    global HEIGHT, WIDTH, screen
    if ((xm > 90 and xm < 225) and (ym > 250 and ym < 290)):
        HEIGHT = 1000
        WIDTH = 1000
    if ((xm > 90 and xm < 200) and (ym > 300 and ym < 330)):
        HEIGHT = 800
        WIDTH = 800
    if ((xm > 90 and xm < 200) and (ym > 350 and ym < 380)):
        HEIGHT = 600
        WIDTH = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
def playGame():
    move = 5    # this means "move 5 pixels"
    # Square variables
    xs = 20
    ys = 20
    wbox = 30
    hbox = 30

    # Circle variables
    rad = 15
    xc = random.randint(rad, WIDTH-rad)
    yc = random.randint(rad, HEIGHT-rad)

    # Inscribe square
    ibox = int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2), int(yc-ibox/2))
    print(startpoint[0]-ibox, startpoint[1])
    insSquare = pygame.Rect(startpoint[0]-ibox, startpoint[1], ibox, ibox)
    
    # Create rect object
    square = pygame.Rect(xs, ys, wbox, hbox)
    # global MAIN
    # idk
    # idk again
    insSquare = pygame.Rect(startpoint[0], startpoint[1], ibox, ibox)
    sq_color = colors.get(randColor)
    MAX=10
    jumpCount=MAX
    JUMP = False
    run = True
    while run:
        screen.fill(background)
        pygame.key.get_pressed() #keys.pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                MAIN = True
                LEV_1 = False

                # print ("I want out", run)
        if keys[pygame.K_ESCAPE]:
            run = False
        if keys[pygame.K_a] and square.x >= move:
            square.x -= move # this subtracts 5 from the x value
        if keys[pygame.K_d] and square.x < WIDTH - wbox:
            square.x += move # this adds 5 to x value
        # Create jump action
        if not JUMP:
            if keys[pygame.K_w]:
                square.y -= move
            if keys[pygame.K_s]:
                square.y += move
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount >=- MAX:
                square.y -= jumpCount * abs(jumpCount) / 2
                jumpCount -= 1
            else:
                jumpCount = MAX
                JUMP = False
    # Finish circle
        if keys[pygame.K_LEFT] and xc >= rad + move:
            xc -= move # subtracts 5 from the x value
            insSquare.x -= move
        if keys[pygame.K_RIGHT] and xc <= WIDTH - (rad + move):
            xc += move # adds 5 to the x value
            insSquare.x += move
        if keys[pygame.K_DOWN] and yc <= HEIGHT - (rad+move):
            yc += move # adds 5 to y value
            insSquare.y += move
        if keys[pygame.K_UP] and yc >= rad + move:
            yc -= move # subtracts 5 from y value
            insSquare.y -= move
        
        checkCollide = square.colliderect(insSquare)
        if checkCollide:
            square.x = random.randint(wbox, WIDTH - wbox)
            square.y = random.randint(hbox, HEIGHT - hbox)
            changeColor()
            sq_color = colors.get(randColor)
            rad += move
            ibox = int(rad * math.sqrt(2))
            startpoint = (int(xc - ibox / 2), int(yc - ibox / 2))
            insSquare = pygame.Rect(startpoint[0], startpoint[1], ibox, ibox)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen, cr_color, insSquare)
        pygame.draw.circle(screen, cr_color, (xc, yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
# sq_color = colors.get('navy')
# Making a rand color of the square
changeColor()
sq_color = colors.get(randColor)
keys = pygame.key.get_pressed()
mouse_pos = (0,1)

first = True 
sc = False
set_first = True
sc_size = False

while check:
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check = False
        if case.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            xm = mouse_pos[0]
            ym = mouse_pos[1]
            print(mouse_pos)
    keys = pygame.key.get_pressed() # this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first = False
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST = False
            MAIN = True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET = False
    if SETT:
        if keys[pygame.K_ESCAPE]:
            SETT = False
            MAIN = True
            sc = False
    if LEV_I:
        screen.fill(background)
        TitleMenu("LEVEL II")
        playGame()
        LEV_I = False
        MAIN = True
        xm = 0
        ym = 0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II = False
            MAIN = True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III = False
            MAIN = True
    if SCORE:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        keepScore()
        # scoreBoard()
        if keys[pygame.K_ESCAPE]:
            SCORE = False
            MAIN = True
    #if SC_SIZE:
    #    screen.fill(background)
    #    TitleMenu("SCREEN SIZE")
    #    MainMenu(SC_sizeList)
    #    set_first = True
    #    changeScreenSize(xm, ym)
    #    if keys[pygame.K_ESCAPE]:
    #        SC_SIZE = False
    #        SETT = True
    if BG_COLOR:
        screen.fill(background)
        TitleMenu("BACKGROUND COLOR")
        if keys[pygame.K_ESCAPE]:
            BG_COLOR = False
            SETT = True
    if SPRITE:
        screen.fill(background)
        TitleMenu("SPRITE")
        if keys[pygame.K_ESCAPE]:
            SPRITE = False
            SETT = True
    if ON_OFF:
        screen.fill(background)
        TitleMenu("SOUND")
        if keys[pygame.K_ESCAPE]:
            ON_OFF = False
            SETT = True
    if ((xm > 90 and xm < 260) and (ym > 250 and ym < 275)) and MAIN:
        MAIN = False
        INST = True
    if ((xm > 90 and xm < 210) and (ym > 300 and ym < 325)) and MAIN:
        MAIN = False
        SETT = True
        xm = 0
        ym = 0
    if ((xm > 90 and xm < 185) and (ym > 350 and ym < 375)) and MAIN:
        MAIN = False
        LEV_I = True
    if ((xm > 90 and xm < 200) and (ym > 400 and ym < 425)) and MAIN:
        MAIN = False
        LEV_II = True
    if ((xm > 90 and xm < 215) and (ym > 450 and ym < 475)) or LEV_III:
        MAIN = False
        LEV_III = True
    if ((xm > 90 and xm < 170) and (ym > 500 and ym < 525)) or SCORE:
        MAIN = False
        SCORE = True
        # screen.fill(background)
    if ((xm > 90 and xm < 260) and (ym > 250 and ym < 275)) and SETT and set_first:
        print("size on")
        screen.fill(background)
        TitleMenu("SCREEN SIZE")
        MainMenu(SC_sizeList)
        SC_SIZE = True
        set_first = False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            set_first = True
            SC_SIZE = False
    if SC_SIZE and xm > 0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("SCREEN SIZE")
        MainMenu(SC_sizeList)
        if keys[pygame.K_ESCAPE]:
            SC_SIZE = False
            set_first = True
    if ((xm > 90 and xm < 210) and (ym > 300 and ym < 325)) and SETT:
        SETT = False
        BG_COLOR = True
    if ((xm > 90 and xm < 185) and (ym > 350 and ym < 375)) and SETT:
        SETT = False
        SPRITE = True
    if ((xm > 90 and xm < 200) and (ym > 400 and ym < 425)) and SETT:
        SETT = False
        ON_OFF = True
    else:
        xm = 0
        ym = 0
        sc = True
    if ((xm > 90 and xm < 130) and (ym > 450 and ym < 475)):
       keepScore(123) # 121 is just a random filler number
       text = INST_FNT.render("Make sure you update the score file", 1, 'black')
       screen.blit(text, (40,200))
       text = INST_FNT.render("before you exit", 1, 'black') # can change this
       screen.blit(text, (40,300))
       text = INST_FNT.render("THANK YOU FOR PLAYING!!!!!", 1, 'red')
       screen.blit(text, (40, 400))
       pygame.display.update()
       pygame.time.delay(50)
       MAIN = False
       SCORE = False
       pygame.time.delay(100)
       check = False
    pygame.display.update()
    pygame.time.delay(10)

os.system('cls')
pygame.quit()



#while check:

#    if MAIN:
#       screen.fill(background)
#        TitleMenu("MENU")
#        MainMenu(MenuList)
#    for case in pygame.event.get():
#        if case.type==pygame.QUIT:
#            check=False
#    keys=pygame.key.get_pressed() #this returns a list
#    if case.type ==pygame.MOUSEBUTTONDOWN:
#        mouse_pos=pygame.mouse.get_pos()
#        print(mouse_pos)
#        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
#            MAIN=False
#            screen.fill(background)
#            TitleMenu("INSTRUCTIONS")
#            INST=True



# def instr():
#    print('in instr')
#    myFile = open('ces-menu\instructions.txt', 'w')
#    yi = 150
#    stuff = myFile.readlines()
#    print(stuff)
#    for line in stuff:
#        print(line)
#        text = INST_FNT.render(line, 1)
#        screen.blit(text, (40,yi))
#        pygame.display.update()
#        pygame.time.delay(50)
#        yi += 50
#    myFile.close()


#def MainMenu(MList):
#    txty=243
#    square.y=250
#    for i in range(len(MList)):
#        message = MenuList[i]
#        text = INST_FNT.render(message,1,'black')
#        screen.blit(text,(90,txty))
#        pygame.draw.rect(screen, 'orange', square)
#        square.y += 50
#        txty += 50

# def scoreboard()
    # stuff.sort()
    # reverse for loop to print the newest score first