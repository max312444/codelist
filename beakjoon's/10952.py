# 문제 10952
# 두 정수 a, b를 입력받은 다음, a + b를 출력하는 프로그램을 작성하시오.

while 1: # while을 사용하여 계속 반복되게 한후 시작
    a, b = map(int,input().split())
    if (a == 0 and b == 0): # a와 b가 0일때 
        break # 멈춤
    else:
        print(a + b) # 그 외의 경우에는 출력