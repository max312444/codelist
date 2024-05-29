# 높이가 5인 다이아 몬드 형태의 별 출력
height = 5
# 위쪽 다이아몬드 형태를 만들어야 하기 위해 높이가 5인 별 삼각형 작성
for i in range(height):
    print(" " * (height - i- 1) + "*" * (2 * i + 1))
# 아래쪽 다이아몬드 형태를 위해 높이가 5인 별 역삼각형 작성
for i in range(height - 2, -1, -1):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))