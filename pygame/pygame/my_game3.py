import pygame
import sys
import random  # random 모듈 임포트

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직임과 장애물 파괴")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 게임 속도 설정
clock = pygame.time.Clock()

# 플레이어 설정
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# 공격 설정
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []

# 장애물 설정
obstacle_width, obstacle_height = 60, 20
obstacles = []

# 떨어지는 물체 설정
falling_object_width, falling_object_height = 40, 40
falling_objects = []
falling_object_speed = 5

# 점수 초기화
score = 0
font = pygame.font.SysFont(None, 36)

# 장애물 생성 타이머 설정
spawn_delay = 800  # 0.8초마다 장애물 생성
last_spawn_time = pygame.time.get_ticks()

# 발사 딜레이 설정
shoot_delay = 300  # 0.3초 딜레이
last_shoot_time = pygame.time.get_ticks()

# 장애물 생존 시간 설정
obstacle_lifetime = 4000  # 4초

# 떨어지는 물체 생성 타이머 설정
falling_spawn_delay = 3000  # 3초마다 떨어지는 물체 생성
last_falling_spawn_time = pygame.time.get_ticks()

def is_colliding_with_existing_obstacles(new_obstacle, obstacles):
    for obstacle, _ in obstacles:
        if new_obstacle.colliderect(obstacle):
            return True
    return False

# 게임 루프
while True:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed + player_size <= screen_width:
        player_x += player_speed
    
    # 발사 딜레이 체크
    if keys[pygame.K_SPACE] and current_time - last_shoot_time > shoot_delay:
        # 총알 발사
        bullet = pygame.Rect(player_x + player_size // 2 - bullet_width // 2, player_y, bullet_width, bullet_height)
        bullets.append(bullet)
        last_shoot_time = current_time  # 마지막 발사 시간 업데이트

    # 장애물 생성
    if current_time - last_spawn_time > spawn_delay:
        while True:
            obstacle_x = random.randint(0, screen_width - obstacle_width)  # 장애물의 x 위치를 무작위로 설정
            obstacle_y = 50
            new_obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
            
            # 다른 장애물들과 겹치지 않는 위치 찾기
            if not is_colliding_with_existing_obstacles(new_obstacle, obstacles):
                obstacles.append((new_obstacle, current_time))  # 장애물과 생성 시간 추가
                last_spawn_time = current_time
                break

    # 장애물 삭제 (생존 시간 3초 초과 시)
    obstacles = [(obstacle, spawn_time) for obstacle, spawn_time in obstacles if current_time - spawn_time < obstacle_lifetime]

    # 떨어지는 물체 생성
    if current_time - last_falling_spawn_time > falling_spawn_delay:
        falling_object_x = random.randint(0, screen_width - falling_object_width)
        falling_object_y = 0
        falling_object = pygame.Rect(falling_object_x, falling_object_y, falling_object_width, falling_object_height)
        falling_objects.append((falling_object, 0))  # 물체와 맞은 횟수 추가
        last_falling_spawn_time = current_time

    # 떨어지는 물체 이동 및 충돌 체크
    for falling_object, hit_count in falling_objects[:]:
        falling_object.y += falling_object_speed
        
        # 플레이어와 충돌 체크
        if falling_object.colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
            print("Game Over")
            pygame.quit()
            sys.exit()
        
        # 화면 밖으로 나간 물체 제거
        if falling_object.y > screen_height:
            falling_objects.remove((falling_object, hit_count))

        # 총알과 충돌 체크
        for bullet in bullets[:]:
            if bullet.colliderect(falling_object):
                bullets.remove(bullet)                
                break

    # 총알 이동 및 충돌 체크
    for bullet in bullets[:]:
        bullet.y -= bullet_speed

        # 총알과 장애물 충돌 체크
        for obstacle, _ in obstacles[:]:
            if bullet.colliderect(obstacle):
                bullets.remove(bullet)
                obstacles.remove((obstacle, _))
                score += 10  # 점수 증가
                break
        
        # 화면 밖으로 나간 총알 제거
        if bullet.y < 0:
            bullets.remove(bullet)

    # 화면 업데이트
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)
    
    # 장애물 그리기
    for obstacle, _ in obstacles:
        pygame.draw.rect(screen, BLUE, obstacle)

    # 떨어지는 물체 그리기
    for falling_object, _ in falling_objects:
        pygame.draw.rect(screen, RED, falling_object)
    
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
