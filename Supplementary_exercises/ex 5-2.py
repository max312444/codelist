# 문제 5-2 별 패턴 그리기 - 상승과 하강
# 자연수 N을 입력 받아서, 지정된 패턴으로 별(*)을 출력한다.
# 첫 번째 줄부터 N번째 줄까지 별의 개수를 1씩 증가시킨다.
# N번째 줄 이후부터는 별의 개수를 감소기켜 마지막 줄에는 별 1개를 출력한다.
N = int(input("N 입력 : ")) # N 값 입력받음
for i in range(1, N + 1): # N번째 줄까지 범위 설정
    print("*" * i) # N번째 줄까지 * 출력
for i in range(N + 1, 2 * N): # N번째 이후 부터 줄어드는 형식 범위 설정 -> for i in range(n-1, 0, -1)과 같다다
    print((2 * N - i)* "*") # 줄어드는 별 범위 출력 

# 교수님 풀이 (for문안에 for문이 있으면 2차원이다.또 있으면 3차원 4차원.....)
# 파이썬에서 제공하는 반복문 종류 두 가지
# 1) for
# 2) while
'''
n = int(input())
for count in range(1, n+1):
    for a in range(0, count):
        print("*", end = "")
    print()
'''