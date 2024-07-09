# 1 ~ 100 사이 정수 중, 3의 배수와 7의 배수를 출력하시오
for i in range(1 , 101):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
        