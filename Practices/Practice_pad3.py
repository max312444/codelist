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

# 함수의 인자 값 4개를 입력받아 합계와 평균을 출력하시오

# def get_num(arg_num1, arg_num2, arg_num3, arg_num4):
    
#     sum = arg_num1 + arg_num2 + arg_num3 + arg_num4
#     avg = sum / 4
#     return sum, avg # 반환값이 2개 이상이면 Tuple로 변환된다.
# sum, avg = get_num(7, 8, 9, 10)
# print(sum, avg)

# def get_num():
#     input_list = [3,4,5,6]
#     get_sum = sum(input_list)
    
#     avg = get_sum / len(input_list)
    
#     print(get_sum)
#     print(avg)
    
#     return sum, avg

# get_num()

# def get_sum_avg(arg_1,arg_2,arg_3,arg_4):
#     input_list = [arg_1,arg_2,arg_3,arg_4]
#     get_sum = sum(input_list)
    
#     avg = get_sum / len(input_list)
    
#     print(get_sum)
#     print(avg)
    
#     return sum, avg

# sum, avg = get_sum_avg(1,2,3,4)

# bar = 3 # 여기서의 bar는 전역변수로 모든 구역에서 사용가능하다.

# def foo(bar):
#     bar = bar + 1 # 여기서의 bar는 지역변수로 함수 밖으로 나가면 삭제된다.
#     print("1: ", bar) # 그래서 여기서는 3에 1을 더한 4가 출력이되고
    
# foo(bar)
# print("2: ", bar) # 함수 밖인 이곳에서는 그냥 3이 출력된다.

# def get_sum(arg_a, arg_b, arg_c):
    
#     sum = arg_a + arg_b + arg_c
#     return sum # return은 2가지 성질이 있는데 그냥 return만 쓰면 함수를 정지시키고 변수를 넣으면 그변수의 값을 전달한다.
# print(get_sum(1,2,3))
# print(get_sum(4,5,6))

# print("------------")
# print(get_sum(7,8,9))

# bar = [3, 4]

# foo = [5, 6]

# kin = bar # bar의 주소값을 같이 사용한다. 

# kin[0] = 1 # kin을 변화를 주면 bar도 같이 변화한다.

# print(bar, foo, kin)

# bar = [3, 4, 5, 6]

# bar[1] = 10

# bar[2] = 20

# bar[0] = 90

# print(bar)

# bar = [2, 3, 5]

# def foo(arg_list):
#     arg_list[1] = 100 # 함수를 설정하여 bar의 1번째 인덱스를 변화시킴
    
# foo(bar)

# print(bar)

# bar = [2, 3, 5]

# def foo(arg_list):
#     copt_list = arg_list[:] # 여기서 bar의 리스트를 복제한다.
    
#     copt_list[0] = 100 # 복제한 리스트의 0번쨰의 값을 100으로 바꿔도 원본의 bar는 값이 변하지 않는다.
    
# foo(bar)
# print(bar)

# def kin(arg_list):
#     arg_list[0] = 200
    
# kin(bar.copy()) # 이것도 위와 같은 뜻이다. 복제한 bar의 리스트의 값을 변화시켰기 떄문에 원본의 bar를 출력하면 그대로이다.

# print(bar)

# def pos(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)
    
# pos(arg_b= 5, arg_a= 2, arg_c= 4) #매개 값을 인자값으로 지정해서  2 5 4 순으로 들어간다.

# def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4): # 초기 값을 지정해놓고 인자값을 입력하지 않으면 초기 값이 출력된다.
#     print(arg_a, arg_b, arg_c, arg_d)
    
# kin() # 인자 값이 없으면 kin의 초기 값을 사용한다.
# kin(6, 7, 8, 9) # 인자 값을 넣어주면 초기 값을 무시하고 넣어준 인자 값을 사용한다.
# kin(6) # 초기 값이 있는 경우엔 인자 값을 매개 변수와 맞추지 않아도 순서대로 들어가고 인자 값이 없는 경우 초기값으로 들어간다.
# kin(6, 7)
# kin(6, 7 , arg_d = 10) # 6, 7은 순서대로 들어가고 3번째는 없으므로 초기값을 사용하고 4번째는 지정해준 값을 넣는다.
# kin(arg_b = 6)

# 구구단 출력하는 프로그램 작성
# 함수로 작성: 2, 3 -> 2단과 3단을 출력
# def printMulTable(arg_start, arg_end=None): # None은 값을 입력하지 않으면 나오게 만듦
#     if arg_end == None: # None이 나오면 
#         for j in range(2, 10): # 한번만 반복
#             print(f"{arg_start} * {j} = {arg_start * j}")
#     else: # 그외 입력시 
#         for i in range(arg_start, arg_end): # 입력한 만큼 단 출력
#             for j in range(2, 10):
#                 print(f"{i} * {j} = {i * j}")
# printMulTable(2, 3)

# def foo(*args):
#     print(len(args))
#     for value in args: # 원소를 나열
#         print(value) 

# foo(1) # 원소의 갯수 : 1
# foo(1,2,3,4,5,6,7,8,9,10,11,12) # 원소의 갯수 : 12

# # 가변 파라메터를 사용해 구구단 출력
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
        
# def foo(**args): # dictionary로 값을 받는다
#     print(len(args)) # 받은 값의 길이구함
#     # for value in args:
#     #     print(value)
#     for key, value in args.items(): # key와 value를 둘다 순회
#         print(f"key: {key}, value : {value}")
#         # 매개 변수 이름에도 관심을 주는 
# foo(test = 2, king = 3) # 1 
# foo(test = 2, king = 3, lion = 4) # 1


# def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
#     print(arg_a, arg_b, arg_c, arg_d, arg_e)
    
# # foo (1,2,3,4,5)

# arg_list = [value for value in range(1, 6)]
# arg_list = [1,2,3,4,5]

# foo(*arg_list) # 콜렉션 언페킹이 일어남 :배열, 리스트, 튜플, 딕셔너리 등과 같은 콜렉션 데이터를 여러 변수에 나누어 할당하는 기법을 의미

# Overloading
# 함수와 메서드에 적용이 된다. 파이썬에서는 지원하지 않는다.
# 사용 목적은? 프로그래머에게 코드 작성의 편리성을 제공하기 위해.
# 기본 위치 인자를 이용하면 함수 오버로딩 기능을 구현 할 수 있다.

# def bar(*args):
#     return sum(args) # sum 함수 사용해서 사용자가 코드 작성을 하기 편하게 만듦

# print(bar(2, 3, 4, 5)) # 14
# print(bar(2, 3, 4)) # 9
# print(bar(2, 3)) # 5

def bar(arg_fnc):
    arg_fnc()
    
def foo():
    print("안녕하세요: ")
    
bar(foo)