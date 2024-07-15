# # Pygame 실행 구조
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True

# while running: # 한번 도는게 그림 한장 그리는 것이다. # 이벤트는 운영체제가 관리함
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     screen.fill((0, 0, 0))
#     pygame.display.flip()
#     clock.tick(60) # while 몇번 돌껀지 - 1초에 그림 60장
    
# pygame.quit()

# # 화면 초기화 및 크기 설정(1)
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# running = True
# while running: 
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
# pygame.quit()

# # 화면 초기화 및 크기 설정 (3)
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# # 화면 가로, 세로 크기 출력
# print(screen.get_width(), screen.get_height())

# # 중심점 좌표 계산
# center_x = int(screen.get_width() / 2)
# center_y = int(screen.get_height() / 2)

# # 색상 정의 # Tuple 형 모든 색상은 RGB를 이용해서 만든다.
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # 점 그리기
# pygame.draw.circle(screen, RED, (center_x, center_y), 40) # 중앙 (화면에, 빨간색, 좌표, 반지름)
# pygame.draw.circle(screen, GREEN, (0, 0), 40) # 왼쪽 상단 모서리
# pygame.draw.circle(screen, BLUE, (799, 599), 40) # 오른쪽 하단 모서리
# pygame.display.flip() # 화면의 업데이트를 관리함. 화면의 깜빡임을 줄이고 부드러운 화면 전환을 가능하게 한다.

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
# pygame.quit()

