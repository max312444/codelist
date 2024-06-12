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

# bar = 3 # 전역 변수 3 

# def foo(bar): # 스택 쌓임
#     bar = bar + 1 # 지역 변수 
#     print("1: ", bar) # 함수 끝나면 bar = 4는 사라짐
    
# foo(bar)

# print("2: ",bar)


# 메모리 주소값을 저장하는 변수 = reference value

# def get_sum (arg_a, arg_b, arg_c): # 인자값 개수와 같다.
    
#     sum = arg_a + arg_b + arg_c
    
#     return sum # 더한 값 전달
# print(get_sum(1, 2, 3)) # 인자값 = 1, 2, 3 총 3개다
# print(get_sum(4, 5, 6))

# print("----------")

# print(get_sum(7, 8, 9))

# bar = [3, 4]

# foo = [5, 6]

# kin = bar

# kin[0] = 1

# print(bar, foo, kin)

# bar = [3, 4, 5, 6]

# bar[1] = 10

# bar[2] = 20

# bar[0] = 90


# bar = [2, 3, 5]

# def foo(arg_list):
#     arg_list[1] = 100
    
    
# foo(bar)

# print(bar) # 2, 100, 5

# bar = [2, 3, 5]

# def foo(arg_list):
#     copy_list = arg_list[:] 
    
#     copy_list[0] = 100
    
    
# foo(bar)

# print(bar) # 2, 3, 5

# def kin(arg_list):
#     arg_list[0] = 200
    
# kin(bar.copy())

# print(bar)

# argument

# 1) positional argument
# 위치 기반으로 인자값은 매개 변수에 순차적으로 들어간다. 

# # 함수를 호출할 떄 정의된 함수의 매개 변수와 인자값의 개수는 무조건 맞춰야 한다.
# def foo(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)
    
# foo(1, 2, 3)

# # 2) keyword argument
# # 매개 변수의 이름을 이용해서 지정해 넣는다.
# # 인자값을 매개변수에 지정해서 넣어서 2, 3, 1 으로 들어간다.
# def pos(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)
    
# pos(arg_c = 1, arg_a = 2, arg_b = 3)

# 3) default argument
# 인자값을 default로 넣을 수 있다. 매개 변수에 초기 값을 넣어줌.
# 1) 모든 파라메터를 초기 값을 정한다.
# 2) 초기 값을 가지는 파라메터는 제일 뒷쪽에 위치한다.
# 3) 초기 값을 가지지 않는 변수와 섞어서 사용하면. 초기 값이 없는 변수는 인자 값을 입력해야한다. 
# def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
#     print(arg_a, arg_b, arg_c, arg_d)
    
# kin() # 인자 값이 없으면 kin의 초기 값을 사용한다.
# kin(6, 7, 8, 9) # 인자 값을 넣어주면 초기 값을 무시하고 넣어준 인자 값을 사용한다.
# kin(6) # 초기 값이 있는 경우엔 인자 값을 매개 변수와 맞추지 않아도 순서대로 들어가고 인자 값이 없는 경우 초기값으로 들어간다.
# kin(6, 7)
# kin(6, 7 , arg_d = 10) # 6, 7은 순서대로 들어가고 3번째는 없으므로 초기값을 사용하고 4번째는 지정해준 값을 넣는다.
# kin(arg_b = 6)


# 함수 안의 매개 변수를 사용할 수도 있고 안할 수도 있다. 
# 앞부분에서 정의하면 에러가 나고 무조건 뒷부분에서 정의해야함

# 매개 변수의 이름 만 매칭 시켜서 대입


# 구구단 출력하는 프로그램 작성
# 함수로 작성: 2, 3 -> 2단과 3단을 출력
# def printMulTable(arg_start, arg_end = None):
#     if arg_end == None:
#         # arg_start = arg_end
#         for j in range(2, 10):
#             print(f"{arg_start} * {j} = {arg_start * j}")
#     else:
#         for i in range(arg_start, arg_end):
#             for j in range(2, 10):
#                 print(f"{i} * {j} = {i * j}")
            
# printMulTable(2)

# def printMulTable(arg_start, arg_end = None):
#     if arg_end == None:
#         arg_end = arg_start
#     # arg_end = arg_start + 1 if arg_end is None else arg_end + 1
#     # for i in range(arg_start, arg_end):
#     #     for j in range(2, 10):
#     #         print(f"{i} * {j} = {i * j}")
#     for i in range(arg_start, arg_end + 1):
#         for j in range(2, 10):
#             print(f"{i} * {j} = {i * j}")
                
# printMulTable(2)



# # variable parameter : 가변 파라메터
# # 1) *
# # 2) **
#         # * -> 가변 : tuple로 받겠다.
# def foo(*args):
#     print(len(args))
#     for value in args: # 원소를 나열
#         print(value) 

# foo(1) # 원소의 갯수 : 1
# foo(1,2,3,4,5,6,7,8,9,10,11,12) # 원소의 갯수 : 12

# 가변 파라메터를 사용해 구구단 출력
# def bar(*args):
#     if len(args) == 1:
#         # 할당(multiple assignment). 한 줄의 코드로 여러 변수에 동일한 값을 할당하는 방법
#         start = end = args[0] 
#     elif len(args) == 2:
#         start, end = args
#     else:
#         return
    
#     for dan in range(start, end + 1):
#         for num in range(1, 10):
#             print(f"{dan} X {num} = {dan*num}")
            
# bar(2)

        # ** -> 가변 : Dictionary(사전형) 로 받겠다.
        #               key(무조건 1개. ex : 주민번호) : value.( ex : 정보)
# def foo(**args):
#     print(len(args))
#     # for value in args:
#     #     print(value)
#     for key, value in args.items():
#         print(f"key: {key}, value : {value}")
#         # 매개 변수 이름에도 관심을 주는 
# foo(test = 2, king = 3) # 1
# foo(test = 2, king = 3, lion = 4) # 1


def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
    print(arg_a, arg_b, arg_c, arg_d, arg_e)
    
# foo (1,2,3,4,5)

arg_list = [value for value in range(1, 6)]
arg_list = [1,2,3,4,5]

foo(*arg_list) # 콜렉션 언페킹이 일어남