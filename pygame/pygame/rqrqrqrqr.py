import pygame
import time

# Pygame 초기화
pygame.init()

# 게임 시작 시점의 시간을 밀리초 단위로 저장
start_time_1 = pygame.time.get_ticks()
print("start_time_1: ", start_time_1) # 236 ms

for i in range(10):
     print("hi")
start_time_2 = pygame.time.get_ticks()
print("start_time_2: ", start_time_2) # 3236
