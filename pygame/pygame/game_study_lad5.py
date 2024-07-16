import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600)) # 화면 설정

# 시작점 (화면 중앙) # 리스트에 넣어서 방향키 입력만큼 값을 늘려줌
start_pos = [(400, 300)]
# 이동 거리
speed = 10
# 처음 시작할때 색상은 랜덤으로
color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
# 반복문 작성
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 키가 눌려지는 것을 인식
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # 왼쪽 누르면 x 값이 이동거리만큼 감소
            new_pos = (start_pos[-1][0] - speed, start_pos[-1][1])
            start_pos.append(new_pos)
        if keys[pygame.K_RIGHT]: # 오른쪽 누르면 x 값이 이동거리만큼 증가
            new_pos = (start_pos[-1][0] + speed, start_pos[-1][1])
            start_pos.append(new_pos)
        if keys[pygame.K_UP]: # 위쪽 누르면 y값이 이동거리만큼 감소
            new_pos = (start_pos[-1][0], start_pos[-1][1] - speed)
            start_pos.append(new_pos)
        if keys[pygame.K_DOWN]: # 아래쪽 누르면 y값이 이동거리만큼 증가
            new_pos = (start_pos[-1][0], start_pos[-1][1] + speed)
            start_pos.append(new_pos)

    # 선 그리기
    if len(start_pos) > 1: 
        for i in range(len(start_pos) - 1): # 리스트 원소내에서 순회
            pygame.draw.line(screen, color, start_pos[i], start_pos[i + 1], 1) # 선 그림

    pygame.display.flip() # 이미지 출력
    
pygame.quit() # 종료


