# 문제 : 10950
# 두 정수 a, b를 입력받은 다음, a+b를 출력하는 프로그램을 작성하시오

t = int(input())
for i in range(t):     #i는 순서를 나타냄
    a, b = map(int,input().split())
    print(a + b)