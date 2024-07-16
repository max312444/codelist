# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# screen.fill((255, 255, 255))
# pygame.display.flip()

# # 원 그리기

# # 색상 정의 
# count = 0 
# random_num = random.randint(5, 20) # 출력할 원의 개수
# # 점 그리기
# while count < random_num: # 나와야하는 원의 개수 보다 count가 커질때
#     color_1 = random.randint(0, 256) # 색을 정하는 1번째 숫자
#     color_2 = random.randint(0, 256) # 색을 정하는 2번째 숫자
#     color_3 = random.randint(0, 256) # 색을 정하는 3번째 숫자
#     x = random.randint(0, 800) # x 좌표 
#     y = random.randint(0, 600) # y 좌표
#     r = random.randint(10, 100) # 원의 반지름 
#     pygame.draw.circle(screen, (color_1, color_2, color_3), (x, y), r)
#     count += 1 # 무한 반복을 막기 위한 count설정
# pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
# pygame.quit()

# # 교수님 추가 풀이
# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# screen.fill((255, 255, 255))
# pygame.display.flip()

# clock = pygame.time.Clock()
# # 원 그리기

# # 색상 정의 
# count = 0 
# random_num = random.randint(5, 21) # 출력할 원의 개수
# # 점 그리기

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     while count < random_num: # 나와야하는 원의 개수 보다 count가 커질때 까지 반복진행
#         color_1 = random.randint(0, 256) # 색을 정하는 1번째 숫자
#         color_2 = random.randint(0, 256) # 색을 정하는 2번째 숫자
#         color_3 = random.randint(0, 256) # 색을 정하는 3번째 숫자
#         x = random.randint(0, 800) # x 좌표 
#         y = random.randint(0, 600) # y 좌표
#         r = random.randint(10, 100) # 원의 반지름 
#         pygame.draw.circle(screen, (color_1, color_2, color_3), (x, y), r)
#         count += 1 # 무한 반복을 막기 위한 count설정
#         pygame.display.flip()
        
#         count = 0 
        
#         clock.tick(30)

# pygame.quit()
