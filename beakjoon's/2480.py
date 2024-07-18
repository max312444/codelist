# 문제 : 2480 주사위 던지기
# 같은 눈이 3개 나오면 10000+ 같은 눈*1000
# 같은 눈이 2개만 나오면 1000+ 같은 눈*100
# 모두 다른 눈 그중 가장 큰눈 * 100

a, b, c = map(int,input().split())
if a == b == c:
    print(10000 +  a * 1000)
elif a == b or b == c or a == c:
    print(1000 + a * 100) if a == c else print(1000 + b * 100)
else:
    print(max(a, b, c)*100)