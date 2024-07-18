# 문제 10810
# 바구니에 1번부터 N번 까지 번호가 있다. 각각의 공은 많이 들고 있다. 가장 처음 바구니에는 공이 없고, 바구니에 공을 1개만 넣을 수 있다.
# M번 공을 넣을 때, 한번 공을 넣을 때, 공을 넣을 바구니의 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀 있는 공을 넣는다. 
# 만약 바구니에 공이 이미 있는 경우에는 공을 뺴고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
N, M = map(int, input().split())

BOX = [0]* N


for _ in range(M):
    i,j,k = map(int, input().split())
    for a in range(i, j+1):
        BOX[a - 1] = k
for i in range(N):
    print(BOX[i], end=' ')