import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
while running: # 함수 = 메소드
    # for - 각각의 이벤트를 순회한다 해당 이벤트에 맞는 함수(메소드)를 호출하면 된다.
    # 이벤트가 발생했을때 특정 이벤트의 행동을 하고 싶으면 for 문 안에 있어야 한다.
    for event in pygame.event.get(): # 현시점에서 쌓여 있던 이벤트들을 순차적으로 가지고 온다. 리스트 형태로
        if event.type == pygame.QUIT:
            running = False
        
    # 이벤트 처리가 끝난 후    
    screen.fill((255, 255, 255)) # 화면 전체를 해당 색깔로 채움. 배경은 제일 먼저 그려줘야함.
    
    pygame.draw.circle(screen, GREEN, (100, 200), 40)
    pygame.draw.circle(screen, RED, (300, 500), 40)
    
    pygame.display.flip()
    
    
pygame.quit()