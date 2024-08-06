import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# 사각형을 X 축으로 이동
# 사각형 생성 (Rect 객체 단위로 묶음)
rect1 = pygame.Rect(0, 50, 80, 60) # rect1은 사각형의 좌표값을 가짐
speed = 500   # 사각형의 X 축 이동 속도

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(120) / 1000

    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    # 사각형을 x, 120 지점에서 그린다. (가로 : 50, 세로: 100)
    pygame.draw.rect(screen, (255, 0, 0), rect1) # Rect 객체 이용
        
    # 사각형의 x 좌표을 5 pixel 우측으로 이동
    rect1.x += speed * dt
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()

pygame.quit()


