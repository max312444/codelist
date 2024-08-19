import pygame
import sys
import random
from itertools import cycle  # 프레임을 순환하기 위해 사용

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1000, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직임과 장애물 파괴")

# GIF 프레임 로드 (GIF를 개별 이미지로 나누어 로드)
obstacle_frames = [pygame.image.load(f"frame_{i}.png") for i in range(1, 10)]  # 1부터 9까지 프레임이 있다고 가정
obstacle_frames_cycle = cycle(obstacle_frames)  # 프레임 순환을 위해 cycle 사용

obstacle_frame_delay = 100  # 각 프레임이 유지되는 시간 (밀리초)
last_obstacle_frame_time = pygame.time.get_ticks()  # 마지막 프레임 전환 시간

# 게임 속도 설정
clock = pygame.time.Clock()

def game_loop():
    global last_obstacle_frame_time

    # 게임 루프 시작
    while True:
        current_time = pygame.time.get_ticks()

        # 장애물 프레임 전환
        if current_time - last_obstacle_frame_time > obstacle_frame_delay:
            current_obstacle_frame = next(obstacle_frames_cycle)
            last_obstacle_frame_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 화면 그리기
        screen.fill((0, 0, 0))  # 검은색 배경

        # 장애물 그리기
        screen.blit(current_obstacle_frame, (100, 100))  # 예시로 (100, 100)에 그립니다.

        pygame.display.flip()
        clock.tick(60)

game_loop()
