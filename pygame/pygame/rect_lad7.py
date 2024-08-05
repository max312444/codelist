import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Movement")

white = (255, 255, 255)

blue_image = pygame.image.load("blue_rect.png")
red_image = pygame.image.load("red_rect.png")

blue_rect = blue_image.get_rect()
blue_rect.topleft = (100, 100)

red_rect = red_image.get_rect()
red_rect.topleft = (200, 200)

speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        blue_rect.x += speed
    if keys[pygame.K_UP]:
        blue_rect.y -= speed
    if keys[pygame.K_DOWN]:
        blue_rect.y += speed
    if keys[pygame.K_a]:
        red_rect.x -= speed
    if keys[pygame.K_d]:
        red_rect.x += speed
    if keys[pygame.K_w]:
        red_rect.y -= speed
    if keys[pygame.K_s]:
        red_rect.y += speed
    
    screen.fill(white)
    
    screen.blit(blue_image, blue_rect)
    screen.blit(red_image, red_rect)
    
    pygame.display.flip()
    
pygame.quit()