import pygame
import random

pygame.init()
screen_width = 480
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("운석 피하기")
clock = pygame.time.Clock()
running = True

player = pygame.image.load("C:\code\pygame\pygame\player.png")
stone = pygame.image.load("C:\code\pygame\pygame\star.png")

player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]

stone_size = stone.get_rect().size
stone_width = stone_size[0]
stone_height = stone_size[1]

player_x_pos = (screen_width / 2) - (player_width / 2)
player_y_pos = screen_height - player_height

stone_x_pos = random.randint(0, (screen_width - player_width))
stone_y_pos = 0

to_x = 0
to_y = 0

speed = 0.5  # 속도 증가
stone_speed = 1  # 속도 증가

game_over_font = pygame.font.Font(None, 100)
game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()
avoid_stone = 0

while running:

    dt = clock.tick(30)
    to_y = 0
    to_y += stone_speed # * dt  # dt 곱하기 추가
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed * dt  # dt 곱하기 추가
            elif event.key == pygame.K_RIGHT:
                to_x += speed * dt  # dt 곱하기 추가
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    player_x_pos += to_x
    stone_y_pos += to_y

    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > (screen_width - player_width):
        player_x_pos = screen_width - player_width

    if stone_y_pos > screen_height:
        stone_x_pos = random.randint(0, screen_width - player_width)
        stone_y_pos = 0
        avoid_stone += 1

    recod_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render('Time: {}'.format(round(recod_time, 2)), True, (255, 255, 255))

    avoided = game_font.render('You avoided: {}'.format(avoid_stone), True, (255, 255, 255))

    game_over = game_over_font.render('Game Over!', True, (255, 255, 255))

    screen.fill((0, 0, 0))  # 화면을 검은색으로 초기화
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(stone, (stone_x_pos, stone_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(avoided, (200, 10))  # screen()이 아닌 screen.blit() 사용

    player_rect = player.get_rect()
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos
    stone_rect = stone.get_rect()
    stone_rect.left = stone_x_pos
    stone_rect.top = stone_y_pos

    if player_rect.colliderect(stone_rect):
        screen.blit(game_over, (50, 100))
        running = False

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
