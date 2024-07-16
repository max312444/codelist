# 1에서 1000사이의 정수 중 3의 배수 합 구하기
# while 문을 사용하여 1~1000까지의 정수 중 3의 배수의 총합을 구하라

# 최종 3의 배수의 합
total_value = 0
# 반복문
while True:
    # 1부터 1000까지 범위 지정
    for input_value in range(1, 1001):
        # 3의 배수 구하는 식
        if input_value % 3 == 0:
            # 3의 배수 더하는 식
            total_value += input_value
    print(total_value)
    break
            