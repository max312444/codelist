import pygame
import random

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Timer Display Example')

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 폰트 설정 (폰트 크기 36)
font = pygame.font.Font(None, 36) # None은 기본 시스템 폰트를 의미

# 타이머 시작 시간
start_time = pygame.time.get_ticks()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 초 단위로 변환
    
    # 화면 초기화
    screen.fill(white)
    
    # 타이머 텍스트 생성
    timer_text = font.render(f"Time: {elapsed_time:.2f} second", True, black)
    
    # 타이머 텍스트 화면에 출력
    screen.blit(timer_text, (10, 10)) # 왼쪽 상단 (10, 10) 위치에 출력
    
    # 화면 업데이트
    pygame.display.flip()
    
pygame.quit()