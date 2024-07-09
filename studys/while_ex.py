# while

# while 조건식:
#       참 일때 실행되는 문장

# 키보드로부터 정수를 입력 받고, 양수일 경우 출력,
# 음수 또는 0인 경우 재입력 -> 양수가 입력 될 떄 까지

# while True:
#     input_num = int(input("정수 입력"))
#     # if input_num < 0:
#     #     print("다시 입력하세요")
#     # else:
#     #     print(input_num,"양수입니다.")
#     #     break
#     if input_num > 0:
#         break
    
# while 문을 이용하여 1에서 10까지 출력하는 프로그램을 작성하라

# count = 1

# # while True:
# #     if count <= 10:
# #         print(count)
# #         count += 1 # 증감식을 놓이는 경우가 있다.
# #     else:
# #         break
    
# while count <= 10:
#         print(count)
#         count += 1 # 증감식을 놓이는 경우가 있다.

bar = ["hello", "world", "Richard"]
# found_word = False # flag 변수 -> 깃발 : Boolean
for word in bar:
    
    if word == "why":
        print("단어를 찾았음")
        found_word = True
        break

# if not found_word:
else: # 정상적으로 반복을 마쳤을 때 실행. 
    print("단어를 찾지 못했음. 나~~빠~~또")
