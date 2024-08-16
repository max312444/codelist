import pygame
import random

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# 색상 정의
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 게임 속도 설정
clock = pygame.time.Clock()
FPS = 90  # FPS를 90으로 고정

# 뱀 설정
snake_block = 20
snake_speed = 0.2  # 뱀의 속도를 0.2로 고정
snake = [(screen_width // 2, screen_height // 2)]  # 뱀의 시작 위치
snake_direction = 'UP'  # 초기 방향

# 이동을 위한 타이머 설정
move_timer = 0

# 먹이 설정
obstacle_image = pygame.image.load("apple.png")
obstacle_size = obstacle_image.get_rect().size

obstacle_x = random.randint(0, screen_width - obstacle_size[0])
obstacle_y = random.randint(0, screen_height - obstacle_size[1])
obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_size[0], obstacle_size[1])

def check_collision(rect1, rect2):
    """ Check if two rectangles collide. """
    return rect1.colliderect(rect2)

def check_self_collision(head, body):
    """ Check if the snake's head collides with its own body. """
    return head in body

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # 시간 누적
    move_timer += snake_speed
    if move_timer >= 1:
        move_timer = 0

        # 뱀 이동
        head_x, head_y = snake[0]
        if snake_direction == 'UP':
            head_y -= snake_block
        elif snake_direction == 'DOWN':
            head_y += snake_block
        elif snake_direction == 'LEFT':
            head_x -= snake_block
        elif snake_direction == 'RIGHT':
            head_x += snake_block

        # 경계선 처리: 뱀의 머리가 화면 밖으로 나가지 않도록
        if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
            running = False

        snake = [(head_x, head_y)] + snake[:-1]  # 뱀의 머리 이동, 꼬리 삭제

        # 먹이 먹기
        snake_head_rect = pygame.Rect(head_x, head_y, snake_block, snake_block)
        if obstacle_rect.colliderect(snake_head_rect):
            snake.append(snake[-1])  # 뱀 길이 증가
            obstacle_x = random.randint(0, screen_width - obstacle_size[0])
            obstacle_y = random.randint(0, screen_height - obstacle_size[1])
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_size[0], obstacle_size[1])

        # 자기 충돌 처리
        if check_self_collision((head_x, head_y), snake[1:]):
            running = False

    # 화면 채우기
    screen.fill(BLACK)

    # 뱀 그리기
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))

    # 먹이 그리기
    screen.blit(obstacle_image, obstacle_rect)

    # 화면 업데이트
    pygame.display.flip()

    # 게임 속도 조절
    clock.tick(FPS)

# 게임 종료
pygame.quit()
