import pygame
from sys import exit
import sys
import time

def autoclicker():
    global score, auto_score
    score += auto_score

def total_buy_upgrade1(score):
    a = score
    if (a / 25) > 1:
        total = int(a/25)
    return total

def total_buy_upgrade2(score):
    a = score
    if (a / 125) >= 1:
        total = int(a/125)
    return total

pygame.init()

mice = 1
score = 10
clickers = 0
auto_score = 0
counter = 0
amount = ['1', 'Max']
amount_chosen = 0

#colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
test_font = pygame.font.Font('Montserrat-ExtraLight.otf', 50)
small_font = pygame.font.Font('Montserrat-ExtraLight.otf', 17)
colour1 = 255
colour2 = 255
colour3 = 255
#music

pygame.mixer.music.load('rise-and-shine.mp3')
pygame.mixer.music.play(1)
effect = pygame.mixer.Sound('crunch.wav')
effect.set_volume(1)

#interface surfaces
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Cookie Clicker 2')
screen.fill(white)
rect = pygame.draw.rect(screen, blue, (0,450,800,200),)
purchase_bar = pygame.draw.rect(screen, blue, (25, 550, 50, 100))
upgrade1 = pygame.draw.rect(screen, white, (25,475,100,100),)
upgrade2 = pygame.draw.rect(screen, white, (150,475,100,100),)
clock = pygame.time.Clock()


#variable surfaces
cookie = pygame.image.load('Cookie.png').convert_alpha()
new_cookie = pygame.transform.scale(cookie,(150, 150))
cookie_x_pos = 325
cookie_y_pos = 155
pointer = pygame.image.load('pointer.png').convert_alpha()
new_pointer = pygame.transform.scale(pointer,(30, 30))
pointer_x_pos = 0
pointer_y_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_RIGHT:
            #   cookie_x_pos += 15

            #if event.key == pygame.K_LEFT:
            #   cookie_x_pos -= 15

            #if event.key == pygame.K_UP:
            #   cookie_y_pos -= 15

            #if event.key == pygame.K_DOWN:
            #   cookie_y_pos += 15
        mouse_pos = pygame.mouse.get_pos()        
        pointer_x_pos, pointer_y_pos = mouse_pos
        if event.type == pygame.MOUSEBUTTONDOWN and pointer_x_pos >= 325 and pointer_x_pos <= 475 and pointer_y_pos >= 155 and pointer_y_pos <= 305:
            score += mice
            effect.play()
        if event.type == pygame.MOUSEBUTTONDOWN and pointer_x_pos >= 25 and pointer_x_pos <= 125 and pointer_y_pos <= 575 and pointer_y_pos >= 475:
            if score >= 25 and amount_chosen == 1:
                clickers += total_buy_upgrade1(score)
                auto_score += total_buy_upgrade1(score)
                score -= total_buy_upgrade1(score)*25
            elif score >= 25:
                clickers += 1
                auto_score += 1
                score -= 25
        if event.type == pygame.MOUSEBUTTONDOWN and pointer_x_pos >= 150 and pointer_x_pos <= 250 and pointer_y_pos <= 575 and pointer_y_pos >= 475:
            if score >= 125 and amount_chosen == 1:
                mice += total_buy_upgrade2(score)
                score -= total_buy_upgrade2(score)*125
            elif score >= 125:
                mice += 1
                score -= 125
        if event.type == pygame.MOUSEBUTTONDOWN and pointer_x_pos >= 25 and pointer_x_pos <= 175 and pointer_y_pos <= 425 and pointer_y_pos >= 375:
            if amount_chosen == 1:
                amount_chosen = 0
            elif amount_chosen == 0:
                amount_chosen = 1

    #changing colour background
    pygame.mouse.set_visible(False)       
    mouse_pos = pygame.mouse.get_pos()
    pointer_x_pos, pointer_y_pos = mouse_pos
    pointer_x_pos -= 15
    pointer_y_pos -= 15
    
    screen.fill((white))
    rect = pygame.draw.rect(screen, blue, (0,450,800,200),) 
    upgrade1 = pygame.draw.rect(screen, white, (25,475,100,100),)
    upgrade2 = pygame.draw.rect(screen, white, (150,475,100,100),)
    purchase_bar = pygame.draw.rect(screen, blue, (25, 375, 150, 50))

    if cookie_x_pos > 725:
        cookie_x_pos = -75
    elif cookie_x_pos < -75:
        cookie_x_pos = 725


    score_surf = test_font.render('Cookies: {}'.format(score), False, 'Black')
    score_rect = score_surf.get_rect(center = (400, 50))

    purchase1_surf = small_font.render('Amount: {}'.format(amount[amount_chosen]), False, 'White')
    purchase1_rect = purchase1_surf.get_rect(center = (100, 400))
    
    upgrade1_surf = small_font.render('Clickers: {}'.format(clickers), False, 'Black')
    upgrade1_rect = upgrade1_surf.get_rect(center = (75, 510))
    upgrade1text_surf = small_font.render('25 coins', False, 'Black')
    upgrade1text_rect = upgrade1text_surf.get_rect(center = (75, 540))
    
    upgrade2_surf = small_font.render('Mice: {}'.format(mice-1), False, 'Black')
    upgrade2_rect = upgrade2_surf.get_rect(center = (200, 510))
    upgrade2text_surf = small_font.render('125 coins', False, 'Black')
    upgrade2text_rect = upgrade2text_surf.get_rect(center = (200, 540))
    

    
    screen.blit(new_cookie,(cookie_x_pos, cookie_y_pos))
    screen.blit(score_surf,score_rect)

    screen.blit(purchase1_surf,purchase1_rect)
    
    screen.blit(upgrade1_surf,upgrade1_rect)
    screen.blit(upgrade1text_surf,upgrade1text_rect)

    screen.blit(upgrade2_surf,upgrade2_rect)
    screen.blit(upgrade2text_surf,upgrade2text_rect)
    
    screen.blit(new_pointer,(pointer_x_pos, pointer_y_pos))

    


    clock.tick(60)
    
    if counter == 30:
        autoclicker()
        counter -= 30
    counter += 1


    pygame.display.update()
