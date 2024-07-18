# 문제 10951
# 두 정수 a 와b를 입력받은 다음, a + b를 출력하는 프로그램을 작성하시오

while True:
    try:
        a, b = map(int,input().split())
        print(a + b)
    except:
        break 
