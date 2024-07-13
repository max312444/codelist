# def print_name(name):
#     print(name, "님 안녕하세요")
    
# print_name("정영철")
# print_name("조원준")

# def sum_total():
#     input_value1 = int(input("첫번째 정수"))
#     input_value2 = int(input("두번째 정수"))
#     input_value3 = int(input("세번째 정수"))
    
#     sum = input_value1 + input_value2 + input_value3
    
#     total = sum/ 3
#     print(sum)
#     print(total)

# sum_total()

# import random


# def get_int(arg_num):
#     input_values = [] # 빈 리스트 생성
#     random_num = random.randint(0, int(input("최대치: ")))
#     for _ in range(arg_num): # 범위 지정 및 생성
#         input_values.append(random_num) # 빈 리스트에 범위 만큼의 수를 입력하여 저장
            
#     return input_values # 값 반환
    
# def get_sum_avg(arg_list): # 합계 평균 구하는 함수 생성
#     sum = 0 # 합계 초기화
#     for value in arg_list:# 입력된 리스트 내의 정수중에서
#         sum += value # 다 더함
    
#     avg = sum / len(arg_list) # 평균은 더한 값을 리스트의 길이로 나누면 된다.1
    
#     return sum, avg # 값 반환

# input_list = get_int(5) # 범위 지정 후 리스트로 지정

# sum, avg = get_sum_avg(input_list) # 리스트를 넣어 리스트 내 정수 합, 평균을 구함

# print(sum, avg)

# def sum(arg_first, arg_second):
#     sum = arg_first + arg_second
    
#     if sum < 0:
#         print("음수")
#         return
#     return sum
# result = sum(2, 3)
# print(result)

# result = sum(-2, -3)
# print(result)

# # 한 개의 정수를 키보드로부터 입력 받아 "짝수", "홀수"를 판별하여 화면에 출력

# def input_value(arg_num):
#     if arg_num % 2 != 0:
#         print("음수")
#     else:
#         print("양수")
        
# input_value(int(input("정수를 입력하세요: ")))

# def get_even_odd(arg_num):
#     msg = "짝수" if arg_num % 2 == 0 else "홀수"
        
#     return msg
# input_value = int(input("정수 입력: "))
# num = get_even_odd(input_value)
# print(num)

# def get_even_odd(arg_num):
#     if arg_num % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
#     return 
# input_value = int(input("정수 입력: "))
# get_even_odd(input_value)

