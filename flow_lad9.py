# range 함수의 세 가지 인자를 사용하여 -10부터 -100까지 10씩 감소하는 숫자 출력
# 시작 숫자 0으로 지정
start_num = 0
# 10번 숫자를 출력하는 범위 설정
for i in range(0, 10):
    # 반복 할때 마다 10씩 감소
    start_num -= 10
    print(start_num)