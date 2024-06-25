msg = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

count = 0
count_lines = 1
count_char = 0
count_word = 0
count_found_word = 0

prev = "" # 이전 글자를 저장하기 위한 변수

find_word = "pos"
find_word_index = 0
find_word_len = len(find_word)
find_word_pos = []

for cur in msg:

    if find_word[find_word_index] == cur:
        find_word_index += 1
        if find_word_index == find_word_len: # 글자를 찾음
            count_found_word += 1
            find_word_index = 0
            find_word_pos.append(count - find_word_len + 1)
    else:
        find_word_index = 0
            
    if cur == " " or cur == "\n":
        if prev != " " and prev != "\n":
            count_word += 1
    elif count == len(msg) - 1: # 마지막 글자
        if prev != " " and prev != "\n":
            count_word += 1
    
    if cur != " " and cur != "\n": 
        count_char += 1
        
    if cur == "\n":
        count_lines += 1
        
    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트

print(f"검색한 단어수: {count_found_word}")
print(f"검색한 단어 위치: {find_word_pos}")
print(f"총 문자수: {count_char}")
print(f"총 줄수: {count_lines}")
print(f"총 단어수: {count_word}")

# 단어의 개수를 셀려고 할때 단어라고 결정하는 경우 3가지
# 1. 공백 기준, 2. 엔터키, 3. 마지막 단어
# 현재글자가 공백 혹은 엔터다. 이전 글자가 문자면 그건 단어다.
# 그럼 현재 글자가 문자가 아니고 이전 글자가 문자이면 단어다.
# 인덱스 - 1을 해서 공백이나 엔터이면 글자가 아니다 
# 첫번째 문제 웬만하면 풀수 있음. 알고리즘 복잡하지 않음
# 두번째 문제 알고리즘은 복잡하지 않은데 해야할 일이 많다. 