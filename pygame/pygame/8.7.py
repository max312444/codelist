import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

count = 0

# 사각형 정의
# rect1 = pygame.Rect(50, 100, 80, 40)
rect1 = pygame.Rect((screen.get_width() - 80) / 2, 100, 80, 40)

# 객체 이동 속도
speed = 500 # 300 pixel / second
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 이벤트 함수를 사용
        # elif event.type == pygame.KEYDOWN: # 키보드가 눌러졌다.
        #     if event.key == pygame.K_LEFT: # 어떤 Key가 눌러졌습니까?
        #         print("왼쪽 화살표 클릭: ", count)
        #         count += 1 
                 

    dt = clock.tick(60) / 1000

    # rect1.x += speed * dt
    # rect1.y += speed * dt
    
    # if rect1.x + rect1.width 값이 > screen.width # 사각형이 화면을 넘어가면
    #    rect1.x = screen.width - rect1.width # 화면에 딱 멈추도록 설정
    
    # if rect1.x + rect1.width > screen.get_width():
    #     rect1.x = screen.get_width() - rect1.width
    #     speed = -speed 
        
    # if 0 > rect1.x:
    #     rect1.x = 0
    #     speed = -speed
    
    # if rect1.y + rect1.height > screen.get_height():
    #     rect1.y = screen.get_height() - rect1.height
    #     speed = -speed
    
    # if rect1.bottom > screen.get_height(): # 위의 코드와 동일
    #     rect1.y = screen.get_height() - rect1.height
    #     speed = -speed
        
    # if 0 > rect1.y:
    #     rect1.y = 0
    #     speed = -speed 
    
    keys = pygame.key.get_pressed()
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        rect1.x = rect1.x - speed * dt
    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        rect1.x += speed *dt

    rect1.x = min(rect1.x + rect1.width, screen.get_width() - rect1.width)
    
    # if rect1.x + rect1.width  > screen.get_width():
    #    rect1.x = screen.get_width() - rect1.width
       
    # if 0 > rect1.x:
    #     rect1.x = 0
        
    # if rect1.y + rect1.height > screen.get_height():
    #     rect1.y = screen.get_height() - rect1.height    

    # if 0 > rect1.y:
    #     rect1.y = 0
    
    # # 좌우 방향키를 누를 때 사각형을 좌우로 이동.
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     rect1.x -= speed * dt
    # if keys[pygame.K_RIGHT]:
    #     rect1.x += speed * dt
    # if keys[pygame.K_UP]:
    #     rect1.y -= speed * dt
    # if keys[pygame.K_DOWN]:
    #     rect1.y += speed * dt
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


