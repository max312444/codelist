# 정수 3개를 입력받아 제일 큰 값 출력하시오

max = -1

for i in range(1,4):
    msg = str(i) + "번"
    input_value = int(input(msg))
    
    if max < input_value:
        max = input_value
        
print(max)

# a = int(input("정수를 입력하세요"))
# b = int(input("정수를 입력하세요"))
# c = int(input("정수를 입력하세요"))

# if a != b != c :
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)
# else:
#     print(a or b or c)
    
# input_1 = int(input("1번"))
# input_2 = int(input("2번"))
# input_3 = int(input("3번"))

# max = input_1

# if max < input_2:
#     max = input_2
    
# if max < input_3:
#     max = input_3
    
# print(max)