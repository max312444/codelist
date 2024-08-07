# 문제 10811
# 바구니 뒤집기
# 바구니 총 N개 가지고 있고, 각 바구니에는 1번부터 N번까지 번호가 적혀져있다. 일렬로 바구니가 놓여있고, 가장 왼쪽부터 1번 ~ N번째 바구니라고 한다.
# M번 바구니의 순서를 역순으로 만들려고 한다. 한번 역순으로 바꿀 때, 역순으로 만들 범위를 정하고, 그 범위 안에 들어있는 바구니의 순서를 역순으로 바꾼다.
# 가장 왼쪽부터 출력하는 프로그램 작성

N, M = map(int, input().split()) # 바구니 수와 몇번 역순으로 바꿀지
box = [value for value in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())  # 역순 바꿀 범위 입력
    # 인덱스는 0부터 시작하므로 i-1, j는 그대로
    box[i-1:j] = reversed(box[i-1:j]) # 범위내 요소 역순으로 바꾸는 함수
         
print(*box)     