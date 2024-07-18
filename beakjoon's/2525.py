# 문제 : 2525
# 시작하는 시각과 필요한 시간이 분단위로 주어졌을 떄, 끝나는 시각을 계산하는 프로그램을 작성하시오.

a, b = map(int,input().split())
c = int(input())
a = a + (c // 60)
b = b + (c % 60)

if b >=60:
    a = a + 1
    b = b - 60
if a >= 24:
    a = a - 24
    
print(a, b)