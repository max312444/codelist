# 문자열 검색 프로그램
# 미리 입력된 문장에서 검색 문자열을 입력 받고,
# 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받음

sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos""" # 총 문자 수(56) 띄어쓰기(11) 개행 문자(2)
sentence = list(sentence)

count = 0 # 단어 포함 개수
words = []
word = ""
index = 0
length = len(sentence)

while index < length:
    char = sentence[index]

    if char == ' ' or char == '\n':
        if word:
            words.append(word)
            word = "" # 초기화
    else:
        word += char # 떨어져있는 알파벳을 ' ' 기준으로 단어로 만드는 과정
    index += 1 
# 마지막 단어 추가
if word:
    words.append(word)
print(words)

while True:
    search_word = input("검색할 문자열을 입력하세요: ")
    if search_word in words:
        for i in words:
            if i == search_word:
                count += 1
        print(f"검색된 문자열의 개수: {count}")
        break
    else:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        
found_index_list = []
while True:
    a = ""
    word_list = list(search_word)
    a = sentence.index(word_list[0])
    found_index_list.append(a)
    # for j in sentence:
    #     if word_list[0] == j:
    #         a = sentence.index(j)
    #         found_index_list.append(a)
    #         a = ""
    print(found_index_list)
    break
