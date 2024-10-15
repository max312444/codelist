import socket
import pygame
import threading

# 클라이언트 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('210.101.236.186', 12345))  # 서버의 IP 주소로 변경하세요

# Pygame 초기화
pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("1대1 게임")

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 플레이어 초기 위치
player_x, player_y = 50, 50
opponent_x, opponent_y = 550, 350

def receive_data():
    global opponent_x, opponent_y
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data:
                opponent_x, opponent_y = map(int, data.split(','))
        except:
            break

# 상대방의 위치를 수신하는 스레드 시작
threading.Thread(target=receive_data, daemon=True).start()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # 현재 위치를 서버에 전송
    client_socket.sendall(f"{player_x},{player_y}".encode())

    # 화면에 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))  # 자신의 캐릭터
    pygame.draw.rect(screen, RED, (opponent_x, opponent_y, 50, 50))  # 상대방 캐릭터

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
client_socket.close()
