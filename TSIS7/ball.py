import pygame
import time
pygame.init()
screen = pygame.display.set_mode((200, 200))
x = 100 # center 
y = 100  # center 
up_limit = 25
down_limit = 175
left_limit = 25
right_limit = 175
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] :
        if(x > right_limit):
            x = right_limit
        x += 0.1
    if keys[pygame.K_LEFT] :
        if(x < left_limit):
            x = left_limit
        x -= 0.1
    if keys[pygame.K_DOWN] :
        if(y > down_limit):
            y = down_limit
        y += 0.1
    if keys[pygame.K_UP] :
        if(y < up_limit):
            y = up_limit
        y -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
