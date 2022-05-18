# learning how to draw circles + rectangles
# use keys to move objects
# using dictionaries

# objective- rectangle runs from circle... if they collide, the circle eats the rectangle
    # circle will get larger + new rectangle should appear somewhere on screen 

import os, random, time, pygame, math
# initialize pygame
pygame.init()

# define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'purple':[48,25,52], 'navy':[5,31,64], 'pink':[200,3,75]}
# get colors
background= 'white'
randColor=''
cr_color= 'purple'

# declare constants, variables, list, dictionaries, any objects
WIDTH=700
HEIGHT=700
move=5
check=True

# create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('CIRCLE EATS SQUARE')
screen.fill(background)
pygame.display.update()
pygame.time.delay(500)

# square variable
xs=20
ys=20
wbox=30
hbox=30

# circle variable
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)

# creating the rectangle
square=pygame.Rect(xs,ys,wbox,hbox)

# Inscribe square
ibox = int(rad*math.sqrt(2))
startpoint = (int(xc-ibox/2), int(yc-ibox/2))
print(startpoint[0]-ibox, startpoint[1])
insSquare = pygame.Rect(startpoint[0]-ibox, startpoint[1], ibox, ibox)

def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        sq_color= colors.get(randColor)
        if colors.get(randColor):
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
sq_color ='navy'
# Making a rand color of the square
# changeColor()

MAX=10
jumpcount=MAX
JUMP=False

check = True
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() # this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move # subtracts 5 from x value
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move
    # Jumping part
    if not JUMP:
        if keys[pygame.K_w]:
            square.y -= move
        if keys[pygame.K_s]:
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP=True
    else:
        if jumpcount >= MAX:
            square.y -= jumpcount*abs(jumpcount)/2
            jumpcount -= 1
        else:
            jumpcount = MAX
            JUMP=False
    # Finish circle
    if keys[pygame.K_LEFT] and xc >= rad + move:
        xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - rad:
        xc += move
    if keys[pygame.K_UP] and yc >= rad + move:
        yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - rad:
        yc += move

    checkCollide = square.collidepoint((xc,yc))
    if checkCollide:
        square.x=random.randint(wbox, WIDTH-rad)
        square.y=random.randint(hbox, HEIGHT-rad)
        changeColor()
        rad += move

    screen.fill(background)
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)

    pygame.display.update()
    pygame.time.delay(10)
