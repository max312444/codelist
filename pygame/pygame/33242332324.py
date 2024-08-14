import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직임과 장애물 파괴")

# 배경음악 파일 로드
background_music = pygame.mixer.music.load("start.mp3")
pygame.mixer.music.play(-1)

# 총소리 파일 로드
sound_fire = pygame.mixer.Sound("shot.mp3")
sound_fire.set_volume(0.5)

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 게임 속도 설정
clock = pygame.time.Clock()

# 플레이어 이미지 로드 및 설정
player_image = pygame.image.load("player1.png")  # 플레이어 이미지 로드
player_size = player_image.get_rect().size  # 이미지 크기 가져오기
player_speed = 5

# 공격 설정
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []

# 장애물 이미지 로드 및 설정
obstacle_image = pygame.image.load("enemy1.png")  # 장애물 이미지 로드
obstacle_size = obstacle_image.get_rect().size  # 이미지 크기 가져오기
obstacles = []

# 장애물 총알 설정
obstacle_bullets = []
obstacle_bullet_speed = 5

# 랜덤한 텀으로 발사 딜레이 설정
obstacle_fire_delay_min = 500  # 최소 0.5초
obstacle_fire_delay_max = 2000  # 최대 2초

# 점수 초기화
score = 0
font = pygame.font.SysFont(None, 36)

# 장애물 생성 타이머 설정
spawn_delay = 800  # 0.8초마다 장애물 생성

# 발사 딜레이 설정
shoot_delay = 300  # 0.3초 딜레이

# 장애물 생존 시간 설정
obstacle_lifetime = 4000  # 4초

def reset_game():
    global player_x, player_y, bullets, obstacles, obstacle_bullets, score, last_shoot_time, last_spawn_time

    # 초기화
    player_x = screen_width // 2 - player_size[0] // 2
    player_y = screen_height - player_size[1] - 10
    bullets = []
    obstacles = []
    obstacle_bullets = []
    score = 0
    last_shoot_time = pygame.time.get_ticks()
    last_spawn_time = pygame.time.get_ticks()

def is_colliding_with_existing_obstacles(new_obstacle, obstacles):
    for obstacle, _, _, _ in obstacles:
        if new_obstacle.colliderect(obstacle):
            return True
    return False

def game_over_screen():
    while True:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over", True, RED)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R 키를 누르면 게임 재시작
                    reset_game()
                    return  # 메인 게임 루프로 복귀
                elif event.key == pygame.K_q:  # Q 키를 누르면 게임 종료
                    pygame.quit()
                    sys.exit()

def game_loop():
    global player_x, player_y, bullets, obstacles, obstacle_bullets, score, last_shoot_time, last_spawn_time
    
    reset_game()  # 게임 루프 시작 시 게임 초기화
    
    while True:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and current_time - last_shoot_time > shoot_delay:
                    # 총알 발사
                    bullet = pygame.Rect(player_x + player_size[0] // 2 - bullet_width // 2, player_y, bullet_width, bullet_height)
                    bullets.append(bullet)
                    sound_fire.play()
                    last_shoot_time = current_time  # 마지막 발사 시간 업데이트

        # 키 입력 처리 (플레이어 이동)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed + player_size[0] <= screen_width:
            player_x += player_speed

        # 장애물 생성
        if current_time - last_spawn_time > spawn_delay:
            while True:
                obstacle_x = random.randint(0, screen_width - obstacle_size[0])  # 장애물의 x 위치를 무작위로 설정
                obstacle_y = 50
                new_obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_size[0], obstacle_size[1])
                
                # 다른 장애물들과 겹치지 않는 위치 찾기
                if not is_colliding_with_existing_obstacles(new_obstacle, obstacles):
                    # 새로운 장애물 생성 및 발사 딜레이와 마지막 발사 시간 초기화
                    obstacle_fire_delay = random.randint(obstacle_fire_delay_min, obstacle_fire_delay_max)
                    last_obstacle_fire_time = current_time
                    obstacles.append((new_obstacle, current_time, last_obstacle_fire_time, obstacle_fire_delay))
                    last_spawn_time = current_time
                    break

        # 장애물 삭제 (생존 시간 4초 초과 시)
        obstacles = [(obstacle, spawn_time, last_fire_time, fire_delay) for obstacle, spawn_time, last_fire_time, fire_delay in obstacles if current_time - spawn_time < obstacle_lifetime]

        # 장애물 총알 발사
        for obstacle in obstacles:
            obstacle_rect, _, last_obstacle_fire_time, obstacle_fire_delay = obstacle
            if current_time - last_obstacle_fire_time > obstacle_fire_delay:
                obstacle_bullet = pygame.Rect(obstacle_rect.x + obstacle_size[0] // 2 - bullet_width // 2, obstacle_rect.y + obstacle_size[1], bullet_width, bullet_height)
                obstacle_bullets.append(obstacle_bullet)
                
                # 발사 후 랜덤한 텀 설정
                obstacles[obstacles.index(obstacle)] = (obstacle_rect, _, current_time, random.randint(obstacle_fire_delay_min, obstacle_fire_delay_max))

        # 장애물 총알 이동 및 충돌 체크
        for obstacle_bullet in obstacle_bullets[:]:
            obstacle_bullet.y += obstacle_bullet_speed

            # 플레이어와 충돌 체크
            if obstacle_bullet.colliderect(pygame.Rect(player_x, player_y, player_size[0], player_size[1])):
                game_over_screen()
                return  # 게임 종료 후 루프를 빠져나가기 위함

            # 화면 밖으로 나간 총알 제거
            if obstacle_bullet.y > screen_height:
                obstacle_bullets.remove(obstacle_bullet)

        # 총알 이동 및 충돌 체크
        for bullet in bullets[:]:
            bullet.y -= bullet_speed

            # 총알과 장애물 충돌 체크
            for obstacle in obstacles[:]:
                obstacle_rect, _, _, _ = obstacle
                if bullet.colliderect(obstacle_rect):
                    bullets.remove(bullet)
                    obstacles.remove(obstacle)
                    score += 10  # 점수 증가
                    break
            
            # 화면 밖으로 나간 총알 제거
            if bullet.y < 0:
                bullets.remove(bullet)

        # 화면 업데이트
        screen.fill(BLACK)
        
        # 플레이어 그리기
        screen.blit(player_image, (player_x, player_y))
        
        # 총알 그리기
        for bullet in bullets:
            pygame.draw.rect(screen, YELLOW, bullet)
        
        # 장애물 그리기
        for obstacle, _, _, _ in obstacles:
            screen.blit(obstacle_image, (obstacle.x, obstacle.y))

        # 장애물 총알 그리기
        for obstacle_bullet in obstacle_bullets:
            pygame.draw.rect(screen, RED, obstacle_bullet) 
        
        # 점수 표시
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)

# 게임 실행
while True:
    game_loop()
