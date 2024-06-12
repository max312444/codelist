# # 문제 17 단어 맞추기 게임
# # 키보드로 영어 단어 3개를 입력 받아 리스트에 저장
# # 단어의 글자 범위는 5 이상 20 이하로 제한
# # 유효 범위를 벗어난 단어를 입력할 경우, 재입력 요구
# # 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
# # 선택된 단어의 글자 중 50%를 Blind 처리
# # 처리된 알페벳은 랜덤하게 선택
# # 올림 알고리즘은 직접 구현하며, 이를 위한 함수를 사용하지 마시오
# # 키보드로부터 알파벳 한글자를 입력받음
# # 입력받은 알파벳이 단어 내에 존재할 경우 Blind 해제
# # 존재하지 않을 경우 "없음" 메시지 출력
# # 단어의 모든 글자를 맞출경우 게임 종료
# # 게임 종료 시 시도 횟수를 출력함

# import random
# num = ["첫", "두", "세"]
# words_list = []
# # 영어 단어 3개 입력 받음 범위는 5 ~ 20사이. 유효 범위 넘을 경우 재입력 요구
# for i in range(3):
#     while True:
#         input_words = input(f"{num[i]}번째 단어를 입력하세요")
#         if 3 <= len(input_words) <= 20:
#             words_list.append(input_words)
#             break
#         else:
#             print("단어의 길이는 3이상 20이하여야 합니다.")

# print(words_list)
    
# # 3개의 단어 중 하나 임의 선택
# random_word = random.choice(words_list)
# print("단어 선택 완료 게임을 시작합니다. 선택된 단어:", random_word)

# random_num_list = list(random_word)
# # 선택한 단어 50% 블라인드 처리
# length = len(random_word)
# blind_a = (length + 1) // 2
# # 중복되지 않은 랜덤 인덱스 번호
# blind_indices = []
# while len(blind_indices) < blind_a:
#     index = random.randint(0, length - 1)
#     if index not in blind_indices:
#         blind_indices.append(index)
# # 뽑은 랜덤 단어를 리스트 화 시킴
# blind_random_word = list(random_word)
# for index in blind_indices: # 리스트의 인덱스 번호에 해당되는 알파벳을 _로 바꿈
#     blind_random_word[index] = '_'
# # 단어로 만들기.
# blind_random_list = ""
# for j in blind_random_word:
#     blind_random_list += j

# # 시도 횟수 
# count = 0

# # 사용자가 알파벳 입력. 입력한 알파벳이 단어 내에 존재하면 블라인드 해제
# while True:
#     print(f"{count + 1}번째 시도, 아래의 단어를 구성하는 알파벳 한 개 입력하세요.")
#     print(blind_random_list)
#     user_input = input("입력")
    
#     for index in range(len(random_num_list)):
#         if user_input == random_num_list[index]:
#             blind_random_word[index] = user_input
#             count += 1
#             print("입력한 알파벳 단어 내 포함 : 개 입니다.")
#             break
# # 없으면 없음 메시지 출력
#         else:
#             print("단어 내 포함되지 않은 알파벳입니다.")
#             count += 1
# # 모두 맞출 경우 게임 종료. 종료시 시도 횟수 출력
#     if '_' not in blind_random_word:
#         print(f"Clear - 선택한 단어: {random_word}. 총 시도 횟수: {count}")
#         break

    

import random

list_words = []

for index in range(3):
    while True:
        input_value = input("단어를 입력하세요: ")
        
        if 5 <= len(input_value) <= 20:
            list_words.append(input_value)
            break
        
        print("5이상 20이하 단어를 입력하세요")
        
word_selected = list(list_words[random.randint(0, 2)])
word_printed = word_selected[:]

print("선택된 단어: ", word_printed)

# 선택된 단어의 글자 수
char_num_word = len(word_selected)

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2

# 반올림 처리 알고리즘 // 연산자는 몫만 가지고 온다.
if blind_num_word > char_num_word // 2:
    blind_num_word += 1
    
blind_num_word = int(blind_num_word)

list_blind_index = [value for value in range(0, char_num_word)]

for index in range(0, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]
    
for index in list_blind_index:
    word_printed[index] = "_"
        
count = 0
        
while len(list_blind_index) > 0:
    print(word_printed)
    
    input_value = input("글짜를 입력하세요: ")
    count += 1
    found_index_list = []
    if input_value in word_selected:
        for index in list_blind_index:
            if word_selected[index] == input_value:
                word_printed[index] = input_value
                found_index_list.append(index)
                
    else:
        print("글자 없음 다시 입력하세요")    
                       
    for f_index in found_index_list:
        list_blind_index.remove(f_index)
    print(f"시도 횟수{count}번")    
print("완성한 단어: ", word_printed)

