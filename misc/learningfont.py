import pygame, time
pygame.init()

WIDTH = 700
HEIGHT = 700
check = True

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("testing")

# font
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('algerian', 40)
INST_FNT=pygame.font.SysFont('comicsans', 25)

fonts = pygame.font.get_fonts()
print(fonts)
print(len(fonts))

screen.fill((255,255,255))
text = TITLE_FNT.render('HEll', 1, (255,0,0))
screen.blit(text,(50,50))
    # "blit"" shows the text on the screen

text = MENU_FNT.render('Test', 1, (0,0,0))
xt = WIDTH / 2 - text.get_width() / 2
screen.blit(text, (xt, 50))

text = INST_FNT.render("Write your instructions here", 1, (0,255,0))
screen.blit(text,(220,220))



# keep window open
while check:
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check = False
    
    pygame.display.update()
    pygame.time.delay(100)