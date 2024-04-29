'''
temp_int = 2

print(type(temp_int))

temp_float = 1.5

print(type(temp_float))

temp_string_1 = "bar"
temp_string_2 = "foo"

print(type(temp_string_1), type(temp_string_2))

temp_bool_1 = True
temp_bool_2 = False

print(type(temp_bool_1), type(temp_bool_2))

if temp_bool_1 :
    print("temp_bool_1 : 참")
else :
    print("temp_bool_1 : 거짓")
    
if temp_bool_2 :
    print("temp_bool_2 : 참")
else :
    print("temp_bool_2 : 거짓")

temp_1 = 1
temp_2 = -1
temp_3 = 0
temp_4 = -0

if temp_1:
    print("참")
else:
    print("거짓")

if temp_2:
    print("참")
else:
    print("거짓")

if temp_3:
    print("참")
else:
    print("거짓")

if temp_4:
    print("참")
else:
    print("거짓")
    
# 선택
# if(조건 하나일 경우), 
# if - else(두 조건 중 무조건 하나 선택일 경우), 
# if - elif...(조건 중 하나를 선택할 수 있고 선택 안할 수 있는 경우),
# if- elif...- else(여러 조건 중 무조건 하나를 선택하는 경우)
# if 시리즈 중에 선택의 최소는 0개 최대는 1개이다 
if 3 > 2:
    print("참 입니다1.")
else:
    print("거짓 입니다1.")

print("프로그램 종료")

if 3 > 2:
    print(1)
elif 3 == 1:
    print(2)
elif 3 == 4:
    print(3)
elif 3 == 5:
    print(4)
    
print("프로그램 종료")

temp_1 = 1
temp_2 = -1
temp_3 = 0
temp_4 = -0

if temp_1:
    print("참")
else:
    print("거짓")
    
if temp_2:
    print("참")
else:
    print("거짓")
    
if temp_3:
    print("참")
else:
    print("거짓")
    
if temp_4:
    print("참")
else:
    print("거짓")

temp_1 = 0
temp_2 = 0.0
temp_3 = ""
temp_4 = None

if temp_1:
    print("참")
else:
    print("거짓")
    
if temp_2:
    print("참")
else:
    print("거짓")
    
if temp_3:
    print("참")
else:
    print("거짓")
    
if temp_4:
    print("참")
else:
    print("거짓")

user_input = "10"
converted_input = int(user_input)
print(converted_input + 5)

str_number = "3.14"
pi = float(str_number)
print(pi * 2)

number = 25
str_number = str(number)
print("The number is : " + str_number)

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

bar = 2

foo = 3

pos = 4

print(bar, foo, pos)

count = 1

while count <= 100000000:
    count = count + 1
    
print("프로그램 종료")

bar = 2

del bar # 메모리를 해제(삭제)하는 명령어

print(bar)

def getAvg(argA, argB, argC):
    sum = argA + argB + argC
    avg = sum / 3
    return avg

result = getAvg(1,2,3)

resilt = getAvg(2,3,4)

result = getAvg(5,6,5)

msg = "hello"

def setting(argMSg):
    msg = argMSg + "hello"
    
setting("안녕하세요")

print(msg)

def bar():
    msg = "안녕하세요"
    foo()
    return msg

def foo():
    print("foo")
    pos()
    print("1")
    kin()
    
def pos():
    print("pos")
    
def kin():
    print("kin")
    
bar()

def foo():
    msg = "hello"
    print(msg)
    

msg = "안녕하세요"

print(msg)

def foo():
    msg = "hello"
    print(greeting)
    

greeting = "안녕하세요"

foo()
'''

def bar():
    local_varable = "지역변수"
    print(local_varable)


global_variable = "전역변수"

bar()

print(local_varable)