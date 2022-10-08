import pygame, random, sys
pygame.init()
import functions1
from functions1 import message, calculator, shop, newsave, save

width = 800
height = 600
white = (255,255,255)
blue = (0,0,255)
color = (255,232,200)
yellow = (255,255,0)
purple = (255,0,255)
black = (0,0,0)

screen = pygame.display.set_mode((width, height))
cookie = pygame.image.load('cookie2.png').convert_alpha()
cookie_rect = cookie.get_rect()
cookie_rect.topleft = (75, 100)
screen.fill(white)

shop1r = pygame.draw.rect(screen, white, (275, 100, 50, 50))
shop2r = pygame.draw.rect(screen, white, (275, 175, 50, 50))
shop3r = pygame.draw.rect(screen, white, (275, 250, 50, 50))
shop4r = pygame.draw.rect(screen, white, (275, 325, 50, 50))

tickvalue = 0
clock = pygame.time.Clock()
Aor1 = '1'

a = save()
a = a.split('+')
coins = int(a[0])
value1 = int(a[1])
value2 = int(a[2])
value3 = int(a[3])
value4 = int(a[4])
c1 = int(a[5])
c2 = int(a[6])
c3 = int(a[7])
c4 = int(a[8])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            newsave(value1, value2, value3, value4, c1, c2, c3, c4, coins)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if cookie_rect.collidepoint(mouse_pos):
                coins += 1
            if shop1r.collidepoint(mouse_pos) and coins >= c1:
                if Aor1 == 'All':
                    value1 += coins//c1
                    c1 = int(c1*(1.1**int(coins//c1)))
                    coins -= coins//c1*c1
                else:
                    value1 += 1
                    coins -= c1
                    c1 = int(c1*1.1)
            elif shop2r.collidepoint(mouse_pos) and coins >= c2:
                if Aor1 == 'All':
                    value2 += coins//c2
                    c2 = int(c2*(1.1**int(coins//c2)))
                    coins -= coins//c2*c2
                else:
                    value2 += 1
                    coins -= c2
                    c2 = int(c2*1.1)
            elif shop3r.collidepoint(mouse_pos) and coins >= c3:
                if Aor1 == 'All':
                    value3 += coins//c3
                    c3 = int(c3*(1.1**int(coins//c3)))
                    coins -= coins//c3*c3
                else:
                    value3 += 1
                    coins -= c3
                    c3 = int(c3*1.1)
            elif shop4r.collidepoint(mouse_pos) and coins >= 70:
                if Aor1 == 'All':
                    value4 += coins//c4
                    c4 = int(c4*(1.1**int(coins//c4)))
                    coins -= coins//c4*c4
                else:
                    value4 += 1
                    coins -= c4
                    c4 = int(c4*1.1)
            elif Aor1r.collidepoint(mouse_pos):
                if Aor1 == '1':
                    Aor1 = 'All'
                else:
                    Aor1 = '1'
    
    screen.fill(white)
    
    middle = pygame.draw.rect(screen, purple, (250, 0, 550, 600))
    message(screen, '{}'.format(calculator(coins)), 400, 75)      
    screen.blit(cookie, (75, 100))
    
    Aor1r = pygame.draw.rect(screen, white, (263, 15, 74, 30))
    message(screen, f'Buy {Aor1}', 300, 30, 20)
    
    shop(screen, value1, value2, value3, value4, c1, c2, c3, c4)
    
    total = value1*2 + value2*4 + value3*8 + value4*16
    message(screen, f'Total = {calculator(total)}/s', 650,  50, 20)
    
    if tickvalue == 60:
        coins = coins + value1*2 + value2*4 + value3*8 + value4*16
        tickvalue = 0
    tickvalue += 1
    pygame.display.update()
    clock.tick(60)
