# 1에서 100까지의 범위 내에서 중복되지 않는 랜덤 정수를 생성 후 리스트에 저장한 후 사용자가 입력한 인덱스에 해당하는 값 출력
# 요구사항:
# 1. 랜덤 정수 개수 n입력
# 2. 입력받은 n에 따라, 1부터 100까지의 숫자 중 중복되지 않은 n개의 랜덤 숫자 생성
# 3. 생성된 랜덤 숫자들은 리스트에 저장
# 4. 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받음 (인덱스는 0부터 n-1까지의 값이어야 함)
# 5. 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력
# 제약 조건 : 
# 1. print, input, random.randint, len 외엔 사용 x
# 2. 중복 값 검사를 위해 not in, in 연산자 사용 금지
# 3. 사용자가 입력한 n이 1 미만이거나 100초과할 경우 계속해서 입력받음
# 4. 사용자가 유효하지 않은 인덱스를 입력한 경우, 에러 메시지를 출력
'''
import random

my_list = []

random_number = random.randint(1, 100)
while True:
    inputValue1 = int(input("N값을 입력하세요 (1-100): "))
    if 100 >= inputValue1 >= 1:
        for _ in range(inputValue1):
            my_list.append(random.randint(1, 100))
        print("생성된 리스트:",my_list)
        break
    else:
        print("에러 N은 1이상 100 이하의 정수여야 합니다.")
inputValue2 = int(input("원하는 원소의 인덱스를 입력하세요 (0-4): "))
if 5 > inputValue2 > 0:
    print("선택한 인덱스의 원소:",my_list[inputValue2])
else:
    print("에러: 유효한 인덱스 범위를 벗어났습니다.")
'''

# import random # 내장함수 random 가져옴
# # 랜덤 정 수 개수 n 입력
# n = -1 
# while n < 1 or n > 100:
#     n = int(input("N값을 입력하세요 (1-100): "))
    
# my_list = [] # 리스트 생성
# while len(my_list) < n: # 반복문 작성. 리스트의 길이가 n보다 작을 때
#     new_number = random.randint(1, 100) # 랜덤 정수 선언
#     is_duplicate = False 
#     for number in my_list: # 
#         if new_number == number:
#             is_duplicate = True
#             break
#     if not is_duplicate:
#         my_list.append(new_number)
# print("생성된 리스트:", my_list)
        
# index = -1
# while index < 0 or index >= n:
#     index = int(input("원하는 원소의 인덱스를 입력하세요:"))

# print("선택한 인덱스의 원소: ",my_list[index])


# import random

# n = int(input("N의 값을 입력하세요 (1-100): "))
# generated_random_num = []

# # 5번 시행
# for trial_count in range(0, n):
    
#     found_duplication = True
    
#     while found_duplication:
#         found_duplication = False
#         random_num = random.randint(1, 100)
    
#         for made_num_index in range(0, trial_count):
#             if generated_random_num[made_num_index] == random_num:
#                 # 중복값 발생 -> 랜덤 넘버를 다시 발생해서 처음부터 다시 검색
#                 found_duplication = True
#                 break
        
#         if not found_duplication:
#             break    
    
#     generated_random_num.append(random_num)
    
    
# print(generated_random_num)
# index_number = int(input("원하는 원소의 인덱스를 입력하세요 (0-n): "))
# if n < index_number or index_number < 0:
#     print("에러: 유효한 인덱스의 범위를 벗어났습니다.")
# else:
#     print("선택한 인덱스의 원소:",generated_random_num[index_number])
    
    
import random

generated_random_num = []
while True:
    n = int(input("N의 값을 입력하세요 (1-100): "))
    if 100>= n >=1:
        break
    else:
        print("에러: N은 1 이상 100 이하의 정수여야 합니다.")

# n번 시행
for trial_count in range(0, n):
    
    found_duplication = True
    
    while found_duplication:
        found_duplication = False
        random_num = random.randint(1, 100)
    
        for made_num_index in range(0, trial_count):
            if generated_random_num[made_num_index] == random_num:
                # 중복값 발생 -> 랜덤 넘버를 다시 발생해서 처음부터 다시 검색
                found_duplication = True
                break
        
        if not found_duplication:
            break    
    
    generated_random_num.append(random_num)
    
print(generated_random_num)
while True:    
    index_number = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{n}): "))
    if n < index_number or index_number < 0:
        print("에러: 유효한 인덱스의 범위를 벗어났습니다.")
    else:
        print("선택한 인덱스의 원소:",generated_random_num[index_number])
        break