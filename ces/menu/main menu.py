# Ava Spence
# 3/23/22

import pygame, time
pygame.init()

# Variables
WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30

# List f messages
MenuList=['Instructions', 'Settings', 'Level I', 'Level II', 'Level III', 'Score', '???']

# Get colors
colors= {'black':[0,0,0], 'grey':[128,128,128], 'white':[255,255,255], 'red':[255,0,0], 'orange':[255,128,0], 'yellow':[255,230,0], 'green':[0,204,0], 'blue':[0, 128, 255], 'purple':[153,51,255], 'pink':[255,102,178]}
background = colors.get('pink')
randColor = ''

# Screen
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
# create different type

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('arial', 30)
INST_FNT=pygame.font.SysFont('arial', 30)

# Create title
text=TITLE_FNT.render('main menu', 1, ('red'))
wind.fill(('white'))
# get the width of the text
# x value = WIDTH/2 - wText/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(xt,50))

# Create first button


# Create square for menu

square=pygame.Rect(xs,ys,wb,hb)
txty=243
for i in range(7):
    message=MenuList[i]
    text=MENU_FNT.render(message,1,'black')
    wind.blit(text,(130,txty))
    pygame.draw.rect(wind,'orange',square)
    square.y += 50
    txty += 50
pygame.display.update()
pygame.time.delay(10000)

