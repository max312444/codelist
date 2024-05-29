# while문과 break문을 사용하여 1부터 100 사이의 숫자를 맞추는 게임 작성
# 사용자가 숫자를 맞출 때까지 반복하고, 맞추면 반복 종료
# 정답 숫자는 랜덤 함수를 이용하여 1에서 100사이 임의 정수 선택

import random
# 임의 정수 뽑아내는 식
random_num = random.randint(1, 100)

while True:
    input_value = int(input("1부터 100사이의 숫자를 맞춰보세요: "))
    # 만약 입력값이 랜덤 정수보다 작으면
    if input_value < random_num:
        print("더 큰 숫자입니다.")
    # 만약 입력값이 랜덤 정수보다 크면
    elif input_value > random_num:
        print("더 작은 숫자입니다.")
    # 입력값이 랜덤 정수와 같으면
    else:
        print("정답입니다!")
        break