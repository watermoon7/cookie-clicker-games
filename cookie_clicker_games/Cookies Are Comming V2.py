import pygame
from sys import exit
import sys
import time

pygame.init()

class Button():
    
    def __init__(self, w, h, posx, posy, c, s):
        self.width = w
        self.height = h
        self.colour = c
        self.pos_x = posx
        self.pos_y = posy
        self.screen = s

    def create(self, w, h, x, y, screen):
        box = pygame.draw.rect(screen, self.colour, (self.pos_x, self.pos_x, self.width, self.height))



red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


screen = pygame.display.set_mode((900, 600))
background_sky = pygame.image.load('background.png')
background_sky = pygame.transform.scale(background_sky,(900, 600))

clock = pygame.time.Clock()
game_running = True

while game_running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_sky,(0,0))
    upgrade_bar = Button(900, 100, 800, 200, blue, screen)
    screen.blit(upgrade_bar.create(900, 100, 800, 200))
    
    clock.tick(60)
    pygame.display.update()
