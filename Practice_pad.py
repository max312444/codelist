import random

# 단어 입력
list_word = []

for index in range(3):
    while True:
        input_value = input("단어 입력: ")

        if 5 <= len(input_value) <= 20:
            list_word.append(input_value)
            break
    
        print("5이상 20이하 단어 입력")

# 단어 선택
word_selected = list(list_word[random.randint(0, 2)])
word_printed = word_selected[:]

print("선택 단어: ", word_printed)
# 단어 블라인드 처리
cha_num_word = len(word_selected)

blind_num_word = cha_num_word / 2

if blind_num_word > cha_num_word // 2:
    blind_num_word += 1
    
blind_num_word = int(blind_num_word)

list_blind_index = [value for value in range(0, cha_num_word)]

for index in range(0, cha_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]
    
for index in list_blind_index:
    word_printed[index] = "_"

# 게임 시작
count = 0

while len(list_blind_index) > 0:
    print(word_printed)
# 알파벳 입력
    input_value = input("글자 입력: ")
    count += 1
    found_index_list = []
    if input_value in word_selected:
        for index in list_blind_index:
            if word_selected[index] == input_value:
                word_printed[index] = input_value
                found_index_list.append(index)
    else:
        print("단어 없음")
        
    for f_index in list_blind_index:
        list_blind_index.remove(f_index)
    print(f"시도 횟수 {count}번")
print("완성된 단어: ", word_printed)

# blind해제

# 게임종료

# 결과 출력