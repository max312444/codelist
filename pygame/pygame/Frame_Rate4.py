import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

x = screen.get_width() / 2
y = screen.get_height() / 2

new_pos = (x, y)
speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_pos = (x - speed, y)
        if keys[pygame.K_RIGHT]:
            new_pos = (x + speed, y)
        if keys[pygame.K_UP]:
            new_pos = (x , y - speed)
        if keys[pygame.K_DOWN]:
            new_pos = (x , y + speed)
    
    pygame.draw.line(screen, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), new_pos, 1)
    
    pygame.display.flip()

pygame.quit()