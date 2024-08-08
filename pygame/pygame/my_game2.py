import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Item Collection Game")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 플레이어 설정
player_size = 50
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 30

# 아이템 설정
item_size = 30
item_pos = [random.randint(0, screen_width-item_size), 0]
item_speed = 20

# 점수
score = 0

# 폰트 설정
font = pygame.font.SysFont("monospace", 35)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed

    # 아이템 이동
    item_pos[1] += item_speed

    # 아이템이 화면 아래로 떨어지면 새로운 위치로 리셋
    if item_pos[1] > screen_height:
        item_pos = [random.randint(0, screen_width-item_size), 0]

    # 충돌 감지
    if (player_pos[0] < item_pos[0] < player_pos[0] + player_size or
            player_pos[0] < item_pos[0] + item_size < player_pos[0] + player_size):
        if (player_pos[1] < item_pos[1] < player_pos[1] + player_size or
                player_pos[1] < item_pos[1] + item_size < player_pos[1] + player_size):
            score += 5
            item_pos = [random.randint(0, screen_width-item_size), 0]

    # 화면 그리기
    screen.fill(black)

    # 플레이어 그리기
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))

    # 아이템 그리기
    pygame.draw.rect(screen, red, (item_pos[0], item_pos[1], item_size, item_size))

    # 점수 표시
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.update()

    # FPS 설정
    clock.tick(30)

pygame.quit()
