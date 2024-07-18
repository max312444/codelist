# 문제 : 11021
# 두 정수 a, b 를 입력받은 다음, a + b 를 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(1,n+ 1):
    a, b = map(int,input().split())
    s = (f"Case #{i}:") # "" 사용하는거 잊지 않기.
    print(s ,a + b)