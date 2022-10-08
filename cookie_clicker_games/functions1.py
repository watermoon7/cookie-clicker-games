import pygame, random
pygame.init()

white = (255,255,255)
blue = (0,0,255)
color = (255,232,200)
yellow = (255,255,0)
purple = (255,0,255)
black = (0,0,0)

def message(screen, text, x, y, size = 1, pos = 'center', colour = 'black'):
    white = (255,255,255)
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    purple = (255,0,255)
    black = (0,0,0)

    font = 'optima'
    if size == 1:
        myfont = pygame.font.SysFont(font, 30)
    elif size == 2:
        myfont = pygame.font.SysFont(font, 15)
    elif size == 3:
        myfont = pygame.font.SysFont(font, 10)
    elif size == 4:
        myfont = pygame.font.SysFont(font, 50) 
    else:
        myfont = pygame.font.SysFont(font, size)
    if pos != 'center':
        if pos == 'left':
            ts = myfont.render(text, True, colour)
            tsR = ts.get_rect(midleft = (x, y))
            screen.blit(ts, tsR)
        if pos == 'right':
            ts = myfont.render(text, True, colour)
            tsR = ts.get_rect(midright = (x, y))
            screen.blit(ts, tsR)
    else:    
        ts = myfont.render(text, True, colour)
        tsR = ts.get_rect(center=(x, y))
        screen.blit(ts, tsR)

def calculator(coins):
    import math
    numbers = [
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
        'sextillion',
        'septillion',
        'octillion',
        'nonillion',
        'decillion',
        'undecillion',
        'duodecillion',
        'tredecillion',
        'quatttuor-decillion',
        'quindecillion',
        'sexdecillion',
        'septen-decillion',
        'octodecillion',
        'novemdecillion',
        'vigintillion'
        ]
    if coins != 0:
        tdigits = int(math.log10(coins)/3)
        if tdigits > 1:
            return '{}'.format(str(int(1000*(coins/10**(int(math.log10(coins)/3)*3)))/1000) + f' {numbers[tdigits-2]}')
        else:
            return coins
    else:
        return coins

def test():
    pointers = 0
    coins = 561455215241349389444 #this number is 561.455 quintillion
    possible = coins//19 #calculating highest number of pointers to buy
    
    pointers += possible
    coins -= possible*19
    #as int() rounds down, coins should never be below 0
    
    print(pointers)
    print(coins)
    

def shop(screen, value1, value2, value3, value4, c1, c2, c3, c4):
    shop1r = pygame.draw.rect(screen, white, (275, 100, 50, 50))
    shop1 = message(screen, '1', 300, 125)
    shop1a = message(screen, f'{c1}c - Yash = 2 cookies/s', 335, 125, 20, 'left')
    shop1b = message(screen, '{}'.format(calculator(int(value1))), 750, 125, 20)
    shop2r = pygame.draw.rect(screen, white, (275, 175, 50, 50))
    shop2 = message(screen, '2', 300, 200)
    shop2a = message(screen, f'{c2}c - monkey Theo = 4 cookies/s', 335, 200, 20, 'left')
    shop2b = message(screen, '{}'.format(calculator(int(value2))), 750, 200, 20)
    shop3r = pygame.draw.rect(screen, white, (275, 250, 50, 50))
    shop3 = message(screen, '3', 300, 275)
    shop3a = message(screen, f'{c3}c - sniper monkey = 8 cookies/s', 335, 275, 20, 'left')
    shop3b = message(screen, '{}'.format(calculator(int(value3))), 750, 275, 20)
    shop4r = pygame.draw.rect(screen, white, (275, 325, 50, 50))
    shop4 = message(screen, '4', 300, 350)
    shop4a = message(screen, f'{c4}c - Will = 16 cookies/s', 335, 350, 20, 'left')
    shop4b = message(screen, '{}'.format(calculator(int(value4))), 750, 350, 20)

def test2(coins):
    import math
    numbers = [
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
        'sextillion',
        'septillion',
        'octillion',
        'nonillion',
        'decillion',
        'undecillion',
        'duodecillion',
        'tredecillion',
        'quatttuor-decillion',
        'quindecillion',
        'sexdecillion',
        'septen-decillion',
        'octodecillion',
        'novemdecillion',
        'vigintillion'
        ]
    tdigits = int(math.log10(coins)/3)
    print(math.log10(coins)/3)
    print(int(math.log10(coins)/3))
    print(int(math.log10(coins)/3)*3)
    print(coins/10**(int(math.log10(coins)/3)*3))
    print(int(1000000*(coins/10**(int(math.log10(coins)/3)*3))))
    print(int(1000000*(coins/10**(int(math.log10(coins)/3)*3)))/1000000)
    print(str(int(100000*(coins/10**(int(math.log10(coins)/3)*3)))/100000) + f' {numbers[tdigits-2]}')
    
def test3(c1, coins):
    c1 = int(c1*(1.1**(int(coins//c1))))
    return c1

def key(value1, value2, value3, value4, c1, c2, c3, c4, coins):
    return str(coins)+'+'+str(value1)+'+'+str(value2)+'+'+str(value3)+'+'+str(value4)+'+'+str(c1)+'+'+str(c2)+'+'+str(c3)+'+'+str(c4)

def newsave(value1, value2, value3, value4, c1, c2, c3, c4, coins):
    file = open('saves.txt', 'a')
    file.write(f'{key(value1, value2, value3, value4, c1, c2, c3, c4, coins)}'+'\n')
    file.close()

def save():
    lines = []
    with open('saves.txt') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        count += 1
        print(f'line {count}: {line}')
        
    choice1 = True
    while choice1:
        try:
            choice = int(input('Which save would you like to load?'))
            choice1 = False
        except:
            print('Invalid - please enter a number (e.g. 1)')

    return str(lines[choice-1])

