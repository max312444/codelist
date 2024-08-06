import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colldelist Example")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

obstacles = [
        pygame.Rect(350, 150, 100, 100), # 첫 번째 Rect : (350, 150) 위치, 100X100 크기
        pygame.Rect(300, 300, 150, 50), # 두 번째 Rect : (300, 300) 위치, 150X50 크기
        pygame.Rect(500, 200, 50, 150), # 세 번째 Rect : (500, 200) 위치, 50X150 크기
        pygame.Rect(400, 400, 200, 50) # 네 번째 Rect : (400, 400) 위치, 200X50 크기
]

moving_rect = pygame.Rect(50, 50, 50, 50)

velocity = 300

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    previous_position = moving_rect.topleft
    
    
    dt = clock.tick(60) / 1000.0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt

    collision_index = moving_rect.collidelist(obstacles)   
    if collision_index != -1:
        # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
        print(f"Collision with obstacle {collision_index}")
        moving_rect.topleft = previous_position
        
    screen.fill(white)
    
    for obs in obstacles:
        pygame.draw.rect(screen, blue, obs)
    
    pygame.draw.rect(screen, red, moving_rect)  
      
    pygame.display.flip()
    
pygame.quit()