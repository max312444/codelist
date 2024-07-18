# 문제 10871
# 정수 n개로 이루어진 수열 a와 정수 x가 주어진다. 이때, a에서 x보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n, x = map(int,input().split()) # n과 x의 수 입력
a = list(map(int,input().split())) # a의 목록을 입력. list는 목록을 작성할 때 사용된다.
for i in range(n): # 범위 n 을 설정
    if a[i] < x: # 만약 a에 입력한 수 중, i 번째 수가 x 보다 작은지 판별
        print(a[i], end = " ") # 작은 수를 출력하고 " "을 양끝에 입력하고 프로그램 중지.