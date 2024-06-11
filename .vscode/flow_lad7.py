# 높이가 5인 다이아 몬드 형태의 별 출력
height = 5
# 위쪽 다이아몬드 형태를 만들어야 하기 위해 높이가 5인 별 삼각형 작성
for i in range(height):
    print(" " * (height - i- 1) + "*" * (2 * i + 1))
# 아래쪽 다이아몬드 형태를 위해 높이가 5인 별 역삼각형 작성
for i in range(height - 2, -1, -1):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))
    
# count = 1

# for i in range (1, 10):
#     # 홀수이면 빈공간을 1개 추가하고 * 2개씩 추가.
#     if i % 2 != 0:
#         print(" " * (5-count), "*" * i)
#         count += 1

# count = 1
# for i in range (1, 8):
#     # 홀수이면 빈공간을 1개 늘리고, *을 2개씩 뺀다.
#     if i % 2 != 0:
#         print(" " * count, "*" * (8-i))
#         count += 1