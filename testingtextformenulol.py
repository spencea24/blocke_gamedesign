# Final Game - Menu

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
INSTR = False
SETT = False
STARTGAME = False
SCORE = False
SC_SIZE = False
SPRITE = False
xm = 0
ym = 0
check = True

# creating the rectangle
square = pygame.Rect(xs,ys,wbox,hbox)

# Colors
colors = {
'black':[0,0,0],
'grey':[128,128,128], 
'white':[255,255,255],
'red':[255,0,0],
'orange':[255,128,0],
'yellow':[255,230,0],
'green':[0,204,0],
'blue':[0, 128, 255],
'purple':[153,51,255],
'pink':[255,102,178]
}
# Get colors
background = (228, 219, 184)

# Lists
Menu_Options = ['- PLAY GAME -', '- INSTRUCTIONS -', '- SETTINGS -', '- SCORE -', '- EXIT -']
Settings_Options = ['Screen Size', 'Sprite']
SC_Options = ['600 x 600', '800 x 800', '1000 x 1000']

# Font
TITLE_FNT = pygame.font.SysFont('algerian', 90)
MENU_FNT = pygame.font.SysFont('georgia', 40)
INSTR_FNT = pygame.font.SysFont('arial', 30)
#MENU_FNT_underline =

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Final Project')

# Create square for menu
square = pygame.Rect(xs,ys,wbox,hbox)

# Functions
# Title
def TitleMenu(Message):
    text = TITLE_FNT.render(Message, 1, [185, 121, 85])
    xt = WIDTH / 2 - text.get_width() / 2
    screen.blit(text, (xt, 50))


# Main Menu
def MainMenu(MList):
    txty = 220
    square.y = 250
    for i in range(len(MList)):
        message = MList[i]
        text = MENU_FNT.render(message, 1,[88,88,88])
        blah = WIDTH / 2 - text.get_width() / 2
        screen.blit(text,(blah,txty))
        pygame.draw.rect(screen, 'black', square)
        square.y += 50
        txty += 60
    pygame.display.update()
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
        pygame.time.delay(50)
        yi += 50
    myFile.close()


instr_first = True
sett_first = True
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
        screen.fill(background)
        TitleMenu("test")
        if keys[pygame.K_ESCAPE]:
            STARTGAME = False
            MAIN = True
    if INSTR and instr_first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        instr_first = False
    if INSTR:
        if keys[pygame.K_ESCAPE]:
            INSTR = False
            MAIN = True
    # if SETT and sett_first:
        # screen.fill(background)
        # TitleMenu("SETTINGS")
        # MainMenu(Settings_Options)
        # sett_first = False
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(Settings_Options)
        sett_first = False
        if keys[pygame.K_ESCAPE]:
            SETT = False
            MAIN = True
    if SCORE:
        screen.fill(background)
        TitleMenu("SCORE")
        if keys[pygame.K_ESCAPE]:
            SCORE = False
            MAIN = True

    # Settings options
    if SC_SIZE:
        screen.fill(background)
        TitleMenu("SCREEN SIZE")
        MainMenu(SC_Options)
        if keys[pygame.K_ESCAPE]:
            SC_SIZE = False
            SETT = True
    if SPRITE:
        screen.fill(background)
        TitleMenu("SPRITE")
        if keys[pygame.K_ESCAPE]:
            SPRITE = False
            SETT = True
    
    # Make things clickable
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and MAIN:
        MAIN = False
        STARTGAME = True
    if ((xm > 20 and xm < 50) and (ym > 300 and ym < 330)) and MAIN:
        MAIN = False
        instr_first = True
        INSTR = True
    if ((xm > 20 and xm < 50) and (ym > 350 and ym < 380)) and MAIN:
        MAIN = False
        SETT = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 400 and ym < 430)) and MAIN:
        MAIN = False
        SCORE = True

    pygame.display.update()
    pygame.time.delay(10)


os.system('cls')
pygame.quit()

# sprite = userselect image (input?)