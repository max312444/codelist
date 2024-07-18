# 문제 : 25304
# 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액 을 보고 구매한 물건의 가격과 개수로
# 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

t = int(input()) # 구매한 물건 총 금액
n = int(input()) # 구매한 물건 총 개수
s = 0 # 총 금액
for i in range(1, n + 1): 
    a, b = map(int,input().split())
    s += a*b 
if t == s:  # 총 금액과 구매 한 물건 총금액 일치 하는지
    print('Yes')
else:
    print('No')
