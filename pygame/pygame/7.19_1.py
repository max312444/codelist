import pygame

## <<-- 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

## <<-- FPS 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 30
## -->>

x = screen.get_width() / 2
y = screen.get_height() / 2
speed = 10 # pixel/second
radius = 40
## <<-- 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(fps) / 1000.0
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    x += speed * dt
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
    pygame.display.flip()
    ## <<-- pygame FPS 설정

    ## -->>
## -->> 이미지 생성
    
## -->> 게임 종료
pygame.quit()