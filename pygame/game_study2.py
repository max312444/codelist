# # Event-Driven은 무조건 무한루프(while)가 있다. event_listener, event_handler가 있다.
# import pygame

# # 파이게임 초기화
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Event Listener and Handler Example")
# running = True

# while running:
#     # 이벤트 큐에서 이벤트를 가져옴
#     for event in pygame.event.get(): # 종료되기 전까지 이벤트를 듣고있어야 해서 무한루프를 돈다.
#         # 이벤트 출력           # get이 이벤트를 가져옴
#         print(event)

# # 파이게임 종료
# pygame.quit()

import pygame

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Event Listener and Handler Example")
running = True

def handle_keydown(event):
    if event.key == pygame.K_SPACE:
        print("Spacebar pressed - handled by function.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed - handled by algorithm")
                running = False
            else:
                handle_keydown(event)

pygame.quit()