import pygame

# pygame 초기화
pygame.init()

# 화면 설정: 800픽셀 너비, 600픽셀 높이의 게임 화면을 생성
screen = pygame.display.set_mode((800, 600))

# 시계 객체 생성: 프레임 레이트 관리와 시간 계산을 위한 객체
clock = pygame.time.Clock()

# 원의 초기 위치: 화면 중앙
x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40 # 원의 반지름 설정

# 원의 이동 속도: 초당 100픽셀
speed = 100

# 게임 루프: 게임이 실행되는 동안 반복
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 델타 타임 계산: 마지막 프레임 이후 경과 시간을 초 단위로 변환
    # 이 값은 각 프레임 간의 시간차이로, 게임의 모든 시간 기반 계산에 사용
    dt = clock.tick(30) / 1000.0 # FPS를 30으로 고정, 결과는 초 단위
    
    # 화면 지우기: 전체 화면을 검은색으로 채움
    screen.fill((0, 0, 0))
    
    # 원 그리기: 화면에 빨간색 원을 현재 x, y 위치에 그림
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    
    # 원 위치 업데이트: 속도와 델타 타임을 곱하여 이동 거리 계산
    x += speed * dt
    
    # 경계 처리: 원이 화면 가장자리에 닿으면 방향 전환
    if x - radius <= 0 or x + radius >= screen.get_width():
        speed = -speed # 속도의 부호를 반전시켜 반대 방향으로 이동
        
    # 화면 업데이트: 변경 사항을 화면에 반영
    pygame.display.flip()
    
# pygame 종료 처리: 게임 루프 종료후 Pygame 라이브러리 종료
pygame.quit()