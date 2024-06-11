# # # def 함수명 (매개변수):  -( )의 이유 이 안에있는매개변수를 정의한다. 
# # #     함수 호출 시 실행되는 명령어

# # # 함수 정의 : -> 1번
# # def print_name(name):
# #     print(name, "님 안녕하세요")

# # # 함수 호출 : -> 2번
# # print_name("리차드")
# # print_name("정영철")

# # 정수 3개를 입력받아 합계와 평균을 출력하는 프로그램 작성

# # def sum_total():
# #     input_value_1 = int(input("첫번째 정수"))
# #     input_value_2 = int(input("두번째 정수"))
# #     input_value_3 = int(input("세번째 정수"))
    
# #     sum = input_value_1 + input_value_2 + input_value_3
    
# #     total = sum/3
# #     print(sum)
# #     print(total)
    
    
# # sum_total()
# def get_int(arg_num):
#     input_values = []
#     for _ in range(arg_num):
#         input_values.append(int(input("입력값: ")))
        
#     return input_values

# def get_sum_avg(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     avg = sum / len(arg_list)
    
#     return sum, avg

# def get_sum(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     return sum
 

# input_list = get_int(13)

# sum, avg = get_sum_avg(input_list)

# print(sum, avg)



# def sum (arg_first, arg_second):
#     sum = arg_first + arg_second
    
#     if sum < 0:
#         print("음수")
#         return
    
#     return sum # 두 가지 role -> 1) 함수 종료 2) 값 반환
# result = sum(2, 3)
# print(result) # result -> 5 # 5

# result = (sum(-2, -3))
# print(result)

# 한 개의 정수를 키보드로부터 입력 받아 "짝수", "홀수"를 판별하여 화면에 출력

# def input_values(arg_num):
#     if arg_num % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# input_values(int(input("정수 입력: ")))

# def get_even_odd(arg_num):
#     msg = "짝수" if arg_num % 2 == 0 else "홀수":
    
#     return msg
        
# input_value = int(input("정수 입력: "))        
# get_even_odd()

# 함수의 인자 값 4개를 입력받아 합계와 평균을 출력하시오

# def get_num(arg_num1, arg_num2, arg_num3, arg_num4):
    
#     sum = arg_num1 + arg_num2 + arg_num3 + arg_num4
    
#     avg = sum / 4

#     return sum, avg # 반환값이 2개 이상이면 Tuple로 변환 후 반환한다.(파이썬만 이럼 다른 언어는 안됨)

# sum, avg = get_num(3, 4, 5, 6)

# print(sum, avg)

# def get_nun():
#     input_list = [3, 4, 5, 6]
#     get_sum = sum(input_list)
    
#     avg = get_sum / len(input_list)
    
#     print(get_sum)
#     print(avg)
    
#     return sum, avg

# get_nun()


# sum, avg = get_sum_avg(1, 2, 3, 4) # 10 2.5


# Call-by-value(값 자체를 복사), Call-by-reference ()

bar = 3 # 전역 변수 3 

def foo(bar): # 스택 쌓임
    bar = bar + 1 # 지역 변수 
    print("1: ", bar) # 함수 끝나면 bar = 4는 사라짐
    
foo(bar)

print("2: ",bar)


# 메모리 주소값을 저장하는 변수 = reference value