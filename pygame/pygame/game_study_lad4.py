import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    r = random.randint(10, 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, event.pos, r)
            pygame.display.flip()
pygame.quit()