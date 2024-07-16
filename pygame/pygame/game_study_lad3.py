import pygame

# 파이게임 라이브러리 초기화
pygame.init()

# 640 X 480 픽셀 크기의 화면을 생성
screen = pygame.display.set_mode((640, 480))

# 게임 루프 실행 여부를 결정하는 변수
running = True

# 게임 루프
while running:
    # 이벤트 큐에서 이벤트를 모두 가져와 순차적으로 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 사용자가 윈도우 닫기 버튼을 클릭하면 발생하는 이벤트
            running = False
        elif event.type == pygame.KEYDOWN:
            # 키보드의 키를 누르면 발생하는 이벤트
            # 눌린 키의 이름을 출력
            print(f"key pressed: {pygame.key.name(event.key)}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 버튼을 클릭하면 발생하는 이벤트
            # 클린된 위치와 버튼 번호를 출력
            print(f"Mouse button {event.button} clicked at position {event.pos}")
# 파이게임 종료 처리
pygame.quit()