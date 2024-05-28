


import random

# 입력할 문자 임의로 만들어 놓고 나중에 다 끝났을 때 입력하는거 작성
list_word = ["kkiikk", "aannaaf", "aeekeet"]

word_selected = list(list_word[random.randint(0, 2)])
word_printed = word_selected[:] # 전체 원소를 선택하고 선택된 원소를 다른 리스트에 대입

# 선태된 단어의 글자 수
char_num_word = len(word_selected)

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2
# 반올림 처리 알고리즘 // 연산자는 몫만 가지고 온다. 
if blind_num_word > char_num_word // 2:
    blind_num_word += 1

blind_num_word = int(blind_num_word)

list_blind_index = [value for value in range(0, char_num_word)]

# print("blind index B : ", list_blind_index)

for index in range(0, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]


# print("blind index A : ", list_blind_index)

for index in list_blind_index:
    word_printed[index] = "_"

print("Printed word : ", word_printed)

input_value = input("문장을 입력하세요 : ")

for index in list_blind_index:
    if word_selected[index] == input_value:
        word_printed[index] = input_value

print(word_printed)

