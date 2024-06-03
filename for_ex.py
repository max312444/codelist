# 1에서 20까지 정수로 구성된 리스트를 생성하세요

# num_list = []

# for i in range(1, 21):
#     num_list.append(i)
# print(num_list)


# list comprehension (리스트 컴플리헨션)
# -> 리스트 내 원소 값들을 for 문을 사용하여 동적으로 생성
#   [item for item in item_list if conditional expression]
# 동적 = 프로그램이 실행되고 나서 값들이 결정이 된다.

# list_num = list(i for i in range(1, 21)) 
# print(list_num)

# list_num = [i for i in range(1, 21)]
# print(list_num)

# 7로 초기화된 8개의 원소를 가지는 리스트를 생성하라
# 리스트 안에 반복문을 넣어 만든다. 
# list_num = [7 for _ in range(8)] # 여기서 for 앞에 값은 원소값을 의미한다.
# print(list_num) # [7, 7, 7, 7, 7, 7, 7, 7]

# 3으로 나누어서 0이 되었을때 즉, 3의 배수일 때만 리스트에 추가한다.
# bar = [value for value in range(1, 21) if value % 3 == 0]
# print(bar)

# 아래 리스트 중 'c'가 포함된 단어만 선택해서 리스트로 구성하라
# foo = ["abc", "dcd", "ef", "gh"]

# bar = [value for value in foo if "c" in value]
# print(bar)
# 단어의 글자 수가 3개 이상인 단어만 선택하여 리스트로 생성
# bar = [value for value in foo if len(value) >= 3]
# print(bar)

# 1에서 10사이 정수중, 홀수는 10을 곱하고 짝수는 20을 곱한 리스트를 생성

# 삼항연산자 : 참 if 조건식 else 거짓 -> 수식. 항이 3개

# bar = [value * 20 if value % 2 == 0 else value * 10 for value in range(1, 11)]
# print(bar)

# 두개의 조건식을 둘다 만족시키는 것만 리스트에 추가. and 와 같다
s_list = [value for value in range(1, 21) if value % 3 == 0 if value % 4 == 0]
print(s_list)

