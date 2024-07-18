# 문제 : 15552
#  input 대신 sys.stdin.readline 을 사용할 수 있다. 단, 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip
#  때문에 문자열을 저장하고 싶을 경우 .rstrip을 추가한다.

import sys # import : 다른 모듈에서 (sys) 값을 가져온다. 

n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

