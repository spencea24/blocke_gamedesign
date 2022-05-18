# Final Game - Draft

import os, random, time, pygame, math, datetime

# Initialize pygame
pygame.init()

# Variables
WIDTH = 600
HEIGHT = 600
move = 5
# square
xs = 20
ys = 20
wbox = 30
hbox = 30
MAIN = True
STARTGAME = False
CLEARING = False
PATH1 = False
CONTINUE1 = False
xm = 0
ym = 0
XP = 0
check = True

# creating the rectangle
square = pygame.Rect(xs,ys,wbox,hbox)
# Colors
colors = {'black':[0,0,0], 'grey':[128,128,128], 'white':[255,255,255], 'red':[255,0,0], 'orange':[255,128,0], 'yellow':[255,230,0], 'green':[0,204,0], 'blue':[0, 128, 255], 'purple':[153,51,255], 'pink':[255,102,178]}
# Get colors
background = 'white'

# Lists
Menu_Options = ['Start Game', 'Instructions', 'Settings', 'Score', 'Exit']

# Font
TITLE_FNT = pygame.font.SysFont('arial', 80)
MENU_FNT = pygame.font.SysFont('arial', 40)
INSTR_FNT = pygame.font.SysFont('arial', 30)
QUESTION_FNT = pygame.font.SysFont('arial', 30)
SMALLQUESTION_FNT = pygame.font.SysFont('arial', 20)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Final Project')

# Create square for menu
square = pygame.Rect(xs,ys,wbox,hbox)

# Images
forest = pygame.image.load('final project\images\Forest.png')

# Functions
# Title
def TitleMenu(Message):
    text = TITLE_FNT.render(Message, 1, 'black')
    screen.fill('white')
    xt = WIDTH / 2-text.get_width() /2
    screen.blit(text, (xt, 50))
# Main Menu
def MainMenu(MList):
    txty = 243
    square.y=250
    for i in range(len(MList)):
        message = MList[i]
        text = INSTR_FNT.render(message, 1,'black')
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen, 'black', square)
        square.y += 50
        txty += 50
    pygame.display.update()
    pygame.time.delay(10)
# Instructions
def instr():
    print('in instr')
    myFile = open('final project\menu\instr.txt', 'r')
    yi = 200
    stuff = myFile.readlines()
    print(stuff)
    for line in stuff:
        print(line)
        text = INSTR_FNT.render(line, 1, 'black')
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(1)
        yi += 50
    myFile.close()
# Hmmmm
#def playgame():


first = True
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

    # Menu options
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(Menu_Options)
    if STARTGAME:
        PATH1 = True
        # playgame()
        screen.blit(forest, (0,0))

        text = SMALLQUESTION_FNT.render("In order to get home, you need to choose a direction to walk in.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 412))

        text = QUESTION_FNT.render('Which way do you go?', 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 472))

        text = INSTR_FNT.render('left', 1, 'red')
        screen.blit(text, (119, 535))

        text = INSTR_FNT.render('right', 1, 'red')
        screen.blit(text, (383, 535))
        pygame.display.update()

        leftpath = ((xm > 95 and xm < 215) and (ym > 523 and ym < 573))
        rightpath = ((xm > 364 and xm < 484) and (ym > 523 and ym < 573))
        if leftpath or rightpath:
            PATH1 = False
            STARTGAME = False
            CONTINUE1 = True
            XP += 100
            print(XP)
            screen.fill(background)
            screen.blit(forest, (0,0))

            text = SMALLQUESTION_FNT.render("Good choice! That took courage. Your bravery has increased your score.", 1, 'white')
            xt = WIDTH / 2 - text.get_width() / 2
            screen.blit(text, (xt, 412))

            text = QUESTION_FNT.render('+100 XP', 1, 'yellow')
            xt = WIDTH / 2 - text.get_width() / 2
            screen.blit(text, (xt, 480))

            text = QUESTION_FNT.render('continue -->', 1, 'white')
            screen.blit(text, (408, 535))
            pygame.display.update()
            xm = 0
            ym = 0
            
            continue1 = ((xm > 405 and xm < 540) and (ym > 540 and ym < 565))
            if continue1:
                xm = 0
                ym = 0
                CONTINUE1 = False
                screen.fill(background)
                pygame.display.update()



    # Make things clickable
    # Menu
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and MAIN:
        MAIN = False
        STARTGAME = True




    pygame.display.update()
    pygame.time.delay(10)


# (40, 403) ------ (560, 403)
# |                         |
# |        question         |
# |                         |
# (40, 453) ------ (560, 453)
# if ((xm > 40 and xm < 560) and (ym > 403 and ym < 453))

# (40, 466) ------ (560, 466)
# |                         |
# |       description       |
# |                         |
# (40, 513) ------ (560, 513)
# if ((xm > 40 and xm < 560) and (ym > 466 and ym < 513))

# (95, 523) ------ (215, 523)
# |                         |
# |        choice 1         |
# |                         |
# (95, 573) ------ (215, 573)
# if ((xm > 95 and xm < 215) and (ym > 523 and ym < 573))

# (364, 523) ------ (484, 523)
# |                         |
# |        choice 2         |
# |                         |
# (364, 573) ------ (484, 573)
# if ((xm > 364 and xm < 484) and (ym > 523 and ym < 573))


os.system('cls')
pygame.quit()

# sprite = userselect image (input?)