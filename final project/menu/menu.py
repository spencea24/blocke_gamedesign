# Final Game - Menu

import os, random, time, pygame, math, datetime
os.system('cls')
name=input("What's your name? \nEnter name: ")
# Initialize pygame
pygame.init()

# Variables
WIDTH = 600
HEIGHT = 600
move = 5
xm = 0
ym = 0
# square
xs = 20
ys = 20
wbox = 30
hbox = 30
# character rectangle
sprx = 80
spry = 80

# menu
MAIN = True
INSTR = False
SETT = False
STARTGAME = False
SCORE = False
SC_SIZE = False
SPRITE = False
EXIT = False
# game
PATH1 = True
CONTINUE1 = False
ENCOUNTER_SLIME = False
ATTACK_SLIME = False
RETREAT1 = False
CONTINUE2 = False
INJURY_SLIMED = False
ENCOUNTER_WOLF = False
XP = 0
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
SC_Options = ['600 x 600', '800 x 800', '900 x 900']

# Font
TITLE_FNT = pygame.font.SysFont('algerian', 90)
MENU_FNT = pygame.font.SysFont('georgia', 40)
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
slime_fight = pygame.image.load('final project\images\Slime_fight.png')
defeated_slime = pygame.image.load('final project\images\Defeated_slime.png')
wolf_fight = pygame.image.load('final project\images\Wolf_fight.png')

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
        pygame.time.delay(1)
        yi += 50
    myFile.close()
def keepXP(XP):
    date = datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(XP) + " " + name + " " + date.strftime('%m/%d/%Y' + '\n')
    # Open a file and write stuff in it.... when you write it erases the previous
    myFile = open('misc\sce.txt', 'w')
    myFile.write(scoreLine)
    myFile.close

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
        check = False
        PlayGame = True
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
    if EXIT:
        pygame.QUIT
        check = False

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
    # Menu
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and MAIN:
        MAIN = False
        STARTGAME = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 300 and ym < 330)) and MAIN:
        MAIN = False
        # instr_first = True
        INSTR = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 350 and ym < 380)) and MAIN:
        MAIN = False
        SETT = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 400 and ym < 430)) and MAIN:
        MAIN = False
        SCORE = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 450 and ym < 480)) and MAIN:
        MAIN = False
        EXIT = True
    # Settings
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and SETT:
        SETT = False
        SC_SIZE = True
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 300 and ym < 330)) and SETT:
        SETT = False
        SPRITE = True
        xm = 0
        ym = 0
    # Screen Size
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and SC_SIZE:
        WIDTH = 600
        HEIGHT = 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 300 and ym < 330)) and SC_SIZE:
        WIDTH = 800
        HEIGHT = 800
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        xm = 0
        ym = 0
    if ((xm > 20 and xm < 50) and (ym > 350 and ym < 380)) and SC_SIZE:
        WIDTH = 900
        HEIGHT = 900
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        xm = 0
        ym = 0

    pygame.display.update()
    pygame.time.delay(10)


while PlayGame:
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            PlayGame = False
        if case.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            xm = mouse_pos[0]
            ym = mouse_pos[1]
            print(mouse_pos)
    keys = pygame.key.get_pressed() # this returns a list

    if RETREAT1:
        # XP RESET

        screen.fill(background)
        screen.blit(forest, (0,0))

        text = SMALLQUESTION_FNT.render("You fall back into the bushes. Coward. Your XP has been reset :(", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 412))

        text = QUESTION_FNT.render('- ALL XP', 1, 'yellow')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 480))

        text = QUESTION_FNT.render('continue -->', 1, 'white')
        screen.blit(text, (408, 535))

    if PATH1:
        screen.fill(background)
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

    if CONTINUE1:
        # +100 XP

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

    if ENCOUNTER_SLIME:
        screen.fill(background)
        screen.blit(slime_fight, (0,0))

        text = SMALLQUESTION_FNT.render("Suddenly, a slime monster jumps out of the bushes!!!!!!", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 412))
        text = SMALLQUESTION_FNT.render("It looks like it wants to fight!!!!!!", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 432))

        text = QUESTION_FNT.render('Draw your sword?', 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 472))

        text = INSTR_FNT.render('yes', 1, 'red')
        screen.blit(text, (119, 535))

        text = INSTR_FNT.render('retreat', 1, 'red')
        screen.blit(text, (383, 535))

    if ATTACK_SLIME:
        screen.fill(background)
        screen.blit(slime_fight, (0,0))

        text = SMALLQUESTION_FNT.render("You can see the slime's brain through its translucent, gelatinous body,", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 400))
        text = SMALLQUESTION_FNT.render("and your adrenaline fills you with strength. If you cut it in half horizontally,", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 420))
        text = SMALLQUESTION_FNT.render("you might miss the brain and get slimed; however, lifting your sword", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 440))
        text = SMALLQUESTION_FNT.render("over your head to cut it in half vertically would take longer than", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 460))
        text = SMALLQUESTION_FNT.render("swinging your sword from the side.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 480))

        text = QUESTION_FNT.render('How do you attack?', 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 500))

        text = INSTR_FNT.render('vertical', 1, 'red')
        screen.blit(text, (119, 535))

        text = INSTR_FNT.render('horizontal', 1, 'red')
        screen.blit(text, (383, 535))

    if CONTINUE2:
        # +75 XP
        screen.fill(background)
        screen.blit(defeated_slime, (0,0))

        text = SMALLQUESTION_FNT.render("Since you know your adrenaline has filled you with strength,", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 400))
        text = SMALLQUESTION_FNT.render("you easily swing your sword down on the slime and cut it in half.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2      
        screen.blit(text, (xt, 420))
        text = SMALLQUESTION_FNT.render("It falls apart instantly.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 440))
        text = SMALLQUESTION_FNT.render("Well done! Your quick thinking has increased your score.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 460))

        text = QUESTION_FNT.render('+75 XP', 1, 'yellow')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 480))

        text = QUESTION_FNT.render('continue -->', 1, 'white')
        screen.blit(text, (408, 535))

    if INJURY_SLIMED:
        # -25 XP
        screen.fill(background)
        screen.blit(forest, (0,0))

        text = SMALLQUESTION_FNT.render("You swing to cut the slime in half horizontally!!!", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 400))
        text = SMALLQUESTION_FNT.render("… but you miss the brain by an inch. Whoops. The slime", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 420))
        text = SMALLQUESTION_FNT.render("charges you and covers you in goop before shimmying back into the bushes.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 440))
        text = SMALLQUESTION_FNT.render("Your injury has decreased your XP.", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 460))

        text = QUESTION_FNT.render('+75 XP', 1, 'yellow')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 480))

        text = QUESTION_FNT.render('continue -->', 1, 'white')
        screen.blit(text, (408, 535))

    if ENCOUNTER_WOLF:
        screen.fill(background)
        screen.blit(wolf_fight, (0,0))
        text = SMALLQUESTION_FNT.render("Suddenly, a wolf approaches you!!!", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 412))
        text = SMALLQUESTION_FNT.render("It looks like it wants to fight!!!!!!", 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 432))

        text = QUESTION_FNT.render('Draw your sword?', 1, 'white')
        xt = WIDTH / 2 - text.get_width() / 2
        screen.blit(text, (xt, 472))

        text = INSTR_FNT.render('yes', 1, 'red')
        screen.blit(text, (119, 535))

        text = INSTR_FNT.render('retreat', 1, 'red')
        screen.blit(text, (383, 535))


    # Make things clickable
    # PATH1 CHOICES
    #   Left
    if ((xm > 95 and xm < 215) and (ym > 523 and ym < 573)) and PATH1:
        XP += 100
        print(XP)
        PATH1 = False
        xm = 0
        ym = 0
        CONTINUE1 = True
    #   Right
    if ((xm > 364 and xm < 484) and (ym > 523 and ym < 573)) and PATH1:
        XP += 100
        print(XP)
        PATH1 = False
        xm = 0
        ym = 0
        CONTINUE1 = True
    # CONTINUE1 -->
    if ((xm > 405 and xm < 540) and (ym > 540 and ym < 565)) and CONTINUE1:
        CONTINUE1 = False
        xm = 0
        ym = 0
        ENCOUNTER_SLIME = True
    # ENCOUNTER_SLIME CHOICES
    #   Yes
    if ((xm > 115 and xm < 155) and (ym > 545 and ym < 565)) and ENCOUNTER_SLIME:
        ENCOUNTER_SLIME = False
        xm = 0
        ym = 0
        ATTACK_SLIME = True
    #   Retreat
    if ((xm > 380 and xm < 455) and (ym > 540 and ym < 565)) and ENCOUNTER_SLIME:
        XP -= (XP)
        print(XP)
        ENCOUNTER_SLIME = False
        xm = 0
        ym = 0
        RETREAT1 = True
    # RETREAT1 -->
    if ((xm > 405 and xm < 540) and (ym > 540 and ym < 565)) and RETREAT1:
        RETREAT1 = False
        xm = 0
        ym = 0
        PATH1 = True
    # ATTACK_SLIME CHOICES
    #   Vertical
    if ((xm > 115 and xm < 195) and (ym > 540 and ym < 565)) and ATTACK_SLIME:
        XP += 75
        print(XP)
        ATTACK_SLIME = False
        xm = 0
        ym = 0
        CONTINUE2 = True
    #   Horizontal
    if ((xm > 380 and xm < 490) and (ym > 540 and ym < 565)) and ATTACK_SLIME:
        XP -= 25
        print(XP)
        ATTACK_SLIME = False
        xm = 0
        ym = 0
        INJURY_SLIMED = True
    # CONTINUE2 -->
    if ((xm > 405 and xm < 540) and (ym > 540 and ym < 565)) and CONTINUE2:
        CONTINUE2 = False
        xm = 0
        ym = 0
        ENCOUNTER_WOLF = True
    # INJURY_SLIMED -->
    if ((xm > 405 and xm < 540) and (ym > 540 and ym < 565)) and INJURY_SLIMED:
        INJURY_SLIMED = False
        xm = 0
        ym = 0
        ENCOUNTER_WOLF = True
    # ENCOUNTER_WOLF CHOICES
    # if ((xm > _ and xm < _) and (ym > 540 and ym > 565)) and ENCOUNTER_WOLF:


    pygame.display.update()

os.system('cls')
pygame.quit()

# sprite = userselect image (input?)

# make a function of xm = 0 and ym = 0 ???