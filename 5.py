# 1이상 30이하의 정수 중에, 짝수 이면서 5의 배수를 출력하시오.

# for num in range(1, 31):
#     if num % 2 == 0 and num % 5 == 0:
#         print(num, "\t", end="")
        
# 입력 값이 홀수이면서 3의 배수 값이 면 출력하시오.

# input_value = int(input("정수 값 입력: "))

# if input_value % 2 == 1:
#     if input_value % 3 == 0: # 위의 11번과 12번이 if input_value % 2 == 1 and input_value % 3 == 0: 과 같다.
#         print(input_value)
        
# 정수를 입력 받아, 입력받은 정수를 화면에 출력하라.
# 언제까지? 3의 배수 또는 4의 배수가 입력되면 프로그램 종료하라.

# while True:
#     input_value = int(input("정수를 입력하세요: "))
#     if input_value % 3 == 0 or input_value % 4 == 0:
#         print(input_value)
#         break

for count in range(1, 10):
    print(count % 5, "\t", end="")