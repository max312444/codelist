import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, RED, (x, y), radius)
    x += speed
    if x + radius > screen.get_width() or x - radius < 0:
        speed = -speed
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()