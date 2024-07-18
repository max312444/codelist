# 문제 11022
# 두 정수 a와 b를 입력받은 다음, a + b 를 출력하는 프로그램을 작성하시오

n = int(input())
for i in range(1, n + 1):
    a, b = map(int,input().split())
    c = a + b
    print(f"Case #{i}: {a} + {b} = {c}")