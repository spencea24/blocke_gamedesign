from re import I
from shutil import move
import pygame as p
#initialize pygame
p.init()
win = p.display.set_mode((500,500))
p.display.set_caption("first game")
walkRight = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L9.png')]
char = p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\standing.png')
bg=p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\\bacroung image.jpg')
x = 50
y = 425
width = 64
height = 64
move = 5
Jump = False
jumpCount = 10
left = False
right = False
walkCount = 0
 
def redrawgamewindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 > 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    p.display.update()
   
clock = p.time.Clock()
#mainloop
run = True
while run:
    clock.tick(27)
   
    redrawgamewindow()
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()
    if keys[p.K_LEFT] and x > move:
        x -= move
        left = True
        right = False
    elif keys[p.K_RIGHT] and x < 500 - width - move:
        x += move
        right = True
        left = False
    else:
        left = False
        right = False
        walkCount = 0
    if not (Jump):
        if keys[p.K_SPACE]:
            Jump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            Jump = False
            jumpCount = 10
p.quit