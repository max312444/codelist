import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1000, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직임과 장애물 파괴")

# 배경음악 파일 로드
background_music = pygame.mixer.music.load("start.mp3")
pygame.mixer.music.set_volume(0.7)

# 음악을 특정 시간 간격으로 반복 재생
music_length = 7  # 음악의 길이 (초)
music_played_time = 0  # 음악이 재생된 시간 (밀리초 단위)

def play_music():
    global music_played_time
    pygame.mixer.music.play(loops=-1)  # 무한 반복으로 음악 재생
    music_played_time = pygame.time.get_ticks()  # 음악 재생 시작 시간 기록

play_music()

# 소리 파일 로드
sound_fire = pygame.mixer.Sound("shot.mp3")
sound_fire.set_volume(0.5)

sound_hit = pygame.mixer.Sound("hit.mp3")
sound_hit.set_volume(0.7)

bomb_use_sound = pygame.mixer.Sound("bomb.mp3")
bomb_use_sound.set_volume(0.7)

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 게임 속도 설정
clock = pygame.time.Clock()

# 플레이어 이미지 로드 및 설정
player_image = pygame.image.load("player1.png")
player_size = player_image.get_rect().size
player_speed = 5

# 공격 설정
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []
bullet_double_active = False
bullet_double_end_time = 0
default_shoot_delay = 300
shoot_delay = default_shoot_delay

# 장애물 이미지 로드 및 설정
obstacle_image = pygame.image.load("enemy1.png")
obstacle_size = obstacle_image.get_rect().size
obstacles = []

# 장애물 총알 설정
obstacle_bullets = []
obstacle_bullet_speed = 5

# 랜덤한 텀으로 발사 딜레이 설정
obstacle_fire_delay_min = 500
obstacle_fire_delay_max = 2000

# 아이템 이미지 로드 및 설정
score_double_image = pygame.image.load("score_doudle.png")
score_double_size = score_double_image.get_rect().size
score_doudles = []

bullet_double_image = pygame.image.load("bullet_doudle.png")
bullet_double_size = bullet_double_image.get_rect().size
bullet_doudles = []

bomb_image = pygame.image.load("bomb.png")
bomb_size = bomb_image.get_rect().size
bombs = []

# 점수 초기화
score = 0
font = pygame.font.SysFont(None, 36)

# 장애물 생성 타이머 설정
spawn_delay = 800

# 장애물 생존 시간 설정
obstacle_lifetime = 4000

# 아이템 생성 타이머 설정
item_spawn_delay = 15000
last_item_spawn_time = 0

# 아이템 효과 지속 시간
item_effect_duration = 10000

# 현재 활성화된 아이템과 그 종료 시간
active_item = None
item_end_time = 0

# 아이템 떨어지는 속도 설정
item_fall_speed = 3

# 최고 점수를 저장할 파일 이름
high_score_file = "high_score.txt"

# 폭탄 관련 설정
bomb_count = 1  # 기본적으로 1개의 폭탄을 가지고 시작

def load_high_score():
    """저장된 최고 점수를 파일에서 불러옵니다."""
    try:
        with open(high_score_file, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(new_high_score):
    """새로운 최고 점수를 파일에 저장합니다."""
    with open(high_score_file, "w") as file:
        file.write(str(new_high_score))

def reset_game():
    global player_x, player_y, bullets, obstacles, obstacle_bullets, score, last_shoot_time, last_spawn_time, bullet_double_active, bullet_double_end_time, score_doudles, bullet_doudles, active_item, item_end_time, shoot_delay, bombs, bomb_count

    # 초기화
    player_x = screen_width // 2 - player_size[0] // 2
    player_y = screen_height - player_size[1] - 10
    bullets = []
    obstacles = []
    obstacle_bullets = []
    score = 0
    last_shoot_time = pygame.time.get_ticks()
    last_spawn_time = pygame.time.get_ticks()
    bullet_double_active = False
    bullet_double_end_time = 0
    score_doudles = []
    bullet_doudles = []
    bombs = []
    bomb_count = 1
    active_item = None
    item_end_time = 0
    shoot_delay = default_shoot_delay  # 발사 딜레이 초기화

def is_colliding_with_existing_obstacles(new_obstacle, obstacles):
    for obstacle, _, _, _ in obstacles:
        if new_obstacle.colliderect(obstacle):
            return True
    return False

def is_colliding_with_existing_items(new_item, items):
    for item, _ in items:
        if new_item.colliderect(item):
            return True
    return False

def game_over_screen(high_score):
    while True:
        screen.fill(BLACK)
        pygame.mixer.music.stop()
        game_over_text = font.render("Game Over", True, RED)
        score_text = font.render(f"Your Score: {score}", True, WHITE)
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - 30))
        screen.blit(high_score_text, (screen_width // 2 - high_score_text.get_width() // 2, screen_height // 2 + 10))
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 50))
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
    global player_x, player_y, bullets, obstacles, obstacle_bullets, score, last_shoot_time, last_spawn_time, bullet_double_active, bullet_double_end_time, score_doudles, bullet_doudles, last_item_spawn_time, active_item, item_end_time, shoot_delay, bombs, bomb_count

    high_score = load_high_score()  # 최고 점수 로드
    reset_game()  # 게임 루프 시작 시 게임 초기화
    
    while True:
        current_time = pygame.time.get_ticks()

        # 음악이 특정 시간 간격으로 반복되도록 조정
        if current_time - music_played_time >= music_length * 1000:
            pygame.mixer.music.stop()  # 음악 정지
            play_music()  # 음악 재생

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

                elif event.key == pygame.K_v and bomb_count > 0:
                    # 폭탄 사용
                    bomb_count -= 1
                    bomb_use_sound.play()
                    for obstacle in obstacles[:]:
                        obstacles.remove(obstacle)
                        score += 10  # 장애물 수 만큼 점수 증가

        # 키 입력 처리 (플레이어 이동)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed + player_size[0] <= screen_width:
            player_x += player_speed

        # 장애물 생성
        if current_time - last_spawn_time > spawn_delay:
            obstacle_rect = pygame.Rect(random.randint(0, screen_width - obstacle_size[0]), 0, obstacle_size[0], obstacle_size[1])
            if not is_colliding_with_existing_obstacles(obstacle_rect, obstacles):
                obstacles.append((obstacle_rect, current_time, current_time, random.randint(obstacle_fire_delay_min, obstacle_fire_delay_max)))
            last_spawn_time = current_time

        # 장애물 이동 및 생존 시간 체크
        for obstacle, spawn_time, last_obstacle_fire_time, obstacle_fire_delay in obstacles[:]:
            obstacle.y += 3
            if obstacle.y > screen_height:
                obstacles.remove((obstacle, spawn_time, last_obstacle_fire_time, obstacle_fire_delay))
            elif pygame.Rect(player_x, player_y, player_size[0], player_size[1]).colliderect(obstacle):
                game_over_screen(high_score)

        # 장애물 삭제 (생존 시간 4초 초과 시)
        obstacles = [(obstacle, spawn_time, last_fire_time, fire_delay) for obstacle, spawn_time, last_fire_time, fire_delay in obstacles if current_time - spawn_time < obstacle_lifetime]

        # 장애물 총알 발사
        for obstacle in obstacles:
            obstacle_rect, _, last_obstacle_fire_time, obstacle_fire_delay = obstacle
            if current_time - last_obstacle_fire_time > obstacle_fire_delay:
                obstacle_bullet = pygame.Rect(obstacle_rect.x + obstacle_size[0] // 2 - bullet_width // 2, obstacle_rect.y + obstacle_size[1], bullet_width, bullet_height)
                obstacle_bullets.append(obstacle_bullet)
                
                obstacles[obstacles.index(obstacle)] = (obstacle_rect, _, current_time, random.randint(obstacle_fire_delay_min, obstacle_fire_delay_max))

        # 장애물 총알 이동 및 충돌 체크
        for obstacle_bullet in obstacle_bullets[:]:
            obstacle_bullet.y += obstacle_bullet_speed

            if obstacle_bullet.colliderect(pygame.Rect(player_x, player_y, player_size[0], player_size[1])):
                game_over_screen(high_score)

            if obstacle_bullet.y > screen_height:
                obstacle_bullets.remove(obstacle_bullet)

        # 총알 이동 및 충돌 체크
        for bullet in bullets[:]:
            bullet.y -= bullet_speed

            for obstacle in obstacles:
                obstacle_rect, _, _, _ = obstacle
                if bullet.colliderect(obstacle_rect):
                    bullets.remove(bullet)
                    obstacles.remove(obstacle)
                    sound_hit.play()
                    score += 10
                    break
            
            if bullet.y < 0:
                bullets.remove(bullet)

        # 아이템 생성
        if current_time - last_item_spawn_time > item_spawn_delay:  # 15초에 한 번 아이템 생성
            item_type = random.choice(["score_double", "bullet_double", "bomb"])  # 랜덤 아이템 선택
            if item_type == "score_double":
                item = pygame.Rect(random.randint(0, screen_width - score_double_size[0]), 0, score_double_size[0], score_double_size[1])  # 위에서 떨어지도록 생성
                if not is_colliding_with_existing_items(item, score_doudles):
                    score_doudles.append((item, item_type))
            elif item_type == "bullet_double":
                item = pygame.Rect(random.randint(0, screen_width - bullet_double_size[0]), 0, bullet_double_size[0], bullet_double_size[1])  # 위에서 떨어지도록 생성
                if not is_colliding_with_existing_items(item, bullet_doudles):
                    bullet_doudles.append((item, item_type))
            elif item_type == "bomb":
                item = pygame.Rect(random.randint(0, screen_width - bomb_size[0]), 0, bomb_size[0], bomb_size[1])  # 위에서 떨어지도록 생성
                if not is_colliding_with_existing_items(item, bombs):
                    bombs.append((item, item_type))
            last_item_spawn_time = current_time  # 마지막 아이템 생성 시간 업데이트

        # 아이템 먹기 및 효과 적용
        for item, item_type in score_doudles[:]:
            item.y += item_fall_speed  # 아이템 떨어짐
            if item.y > screen_height:  # 화면 밖으로 나가면 삭제
                score_doudles.remove((item, item_type))
            elif pygame.Rect(player_x, player_y, player_size[0], player_size[1]).colliderect(item):
                score_doudles.remove((item, item_type))
                score *= 2
                active_item = "Score Double"

        for item, item_type in bullet_doudles[:]:
            item.y += item_fall_speed  # 아이템 떨어짐
            if item.y > screen_height:  # 화면 밖으로 나가면 삭제
                bullet_doudles.remove((item, item_type))
            elif pygame.Rect(player_x, player_y, player_size[0], player_size[1]).colliderect(item):
                bullet_doudles.remove((item, item_type))
                bullet_double_active = True
                bullet_double_end_time = current_time + item_effect_duration
                active_item = "Bullet Double"
                item_end_time = current_time + item_effect_duration
                shoot_delay = default_shoot_delay // 2  # 발사 딜레이를 절반으로 줄임

        for item, item_type in bombs[:]:
            item.y += item_fall_speed  # 아이템 떨어짐
            if item.y > screen_height:  # 화면 밖으로 나가면 삭제
                bombs.remove((item, item_type))
            elif pygame.Rect(player_x, player_y, player_size[0], player_size[1]).colliderect(item):
                bombs.remove((item, item_type))
                bomb_count += 1  # 폭탄 수 증가
                active_item = "Bomb"

        # 아이템 효과 시간 경과 확인
        if current_time > item_end_time:
            active_item = None
            if bullet_double_active and current_time > bullet_double_end_time:
                bullet_double_active = False
                shoot_delay = default_shoot_delay  # 발사 딜레이를 원래 값으로 복구

        # 화면 그리기
        screen.fill(BLACK)

        # 플레이어 그리기
        screen.blit(player_image, (player_x, player_y))

        # 장애물 그리기
        for obstacle, _, _, _ in obstacles:
            screen.blit(obstacle_image, obstacle)

        # 총알 그리기
        for bullet in bullets:
            pygame.draw.rect(screen, YELLOW, bullet)

        # 장애물 총알 그리기
        for obstacle_bullet in obstacle_bullets:
            pygame.draw.rect(screen, RED, obstacle_bullet)

        # 아이템 그리기
        for item, _ in score_doudles:
            screen.blit(score_double_image, item)
        for item, _ in bullet_doudles:
            screen.blit(bullet_double_image, item)
        for item, _ in bombs:
            screen.blit(bomb_image, item)

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # 최고 점수 표시
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_text, (10, 50))

        # 폭탄 개수 표시
        bomb_text = font.render(f"Bombs: {bomb_count}", True, WHITE)
        screen.blit(bomb_text, (screen_width - bomb_text.get_width() - 10, 50))

        # 활성화된 아이템 및 남은 시간 표시
        if active_item:
            remaining_time = (item_end_time - current_time) // 1000  # 초 단위로 계산
            item_text = font.render(f"{active_item}: {remaining_time}s left", True, WHITE)
            screen.blit(item_text, (screen_width - item_text.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(60)

        # 게임 오버 시 최고 점수 업데이트 및 저장
        if current_time > item_end_time and not bullet_double_active:
            if score > high_score:
                high_score = score
                save_high_score(high_score)

game_loop()
