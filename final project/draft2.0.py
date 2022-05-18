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
PlayGame = False
# hm
PATH1 = True
CONTINUE1 = False
ENCOUNTER_SLIME = False
ATTACK_SLIME = False
RETREAT1 = False
CONTINUE2 = False
INJURY_SLIMED = False
ENCOUNTER_WOLF = False
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
        text = MENU_FNT.render(message, 1,'black')
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
        check = False
        PlayGame = True

    # Make things clickable
    # Menu
    if ((xm > 20 and xm < 50) and (ym > 250 and ym < 280)) and MAIN:
        MAIN = False
        STARTGAME = True

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


    pygame.display.update()




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