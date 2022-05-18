import os, time
import pygame as p

# initialize pygame
p.init()
# define colors
white=[255,255,255]
red=[255,0,0]
magenta=[255,0,255]
aqua=[51,153,255]
mystery=[47,192,229]

# create your window/screen
WIDTH=600
HEIGHT=700
screen=p.display.set_mode ((WIDTH,HEIGHT))
p.display.set_caption("My Window")
screen.fill(mystery)
p.display.update()
# flash color
p.time.delay(500)
screen.fill(red)
p.display.update()
p.time.delay(500)

# how to draw something:
# define rectangle
# position:
x=20
y=30
# width + heigh:t of rectangle:
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
    # when creating rectangle, use uppercase (Rect), but when putting it in loop, use lowercase (rect)
square2=p.Rect(x+200, y+200, wbox, hbox)



# create "while loop" to keep window open + be able to close it with the X button
# main game loop
run=True
while run:
    screen.fill(magenta)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    square.x+=5 # square will move 5 pixels every time it loops
    square.y+=5 # square will move 5 pixels every time it loops
    p.draw.rect(screen,(white), square)
    p.draw.rect(screen,(red), square2)
    p.display.update()
    p.time.delay(100)