# 문제 13 공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산
# 여러 문장으로 구성된 하나의 문자열을 입력받음
# 이 문자열에서 사용자가 지정한 단어가 몇 번 등장하는지를 카운트하는 프로그램 작성
# 단어와 문장은 공백으로 구분
# 결과는 단어의 출현 횟수 출력
# 조건 : 함수는 input, print, append, insert, len 및 형변환 함수 이외에는 사용 금지 
# in, not in 연산자 사용하지 마시오
# 두 번의 입력을 받음. 첫 번째 입력은 검사할 전체 문자열이며, 두 번째 입력은 출현 빈도를 확인할 단어

inputvalue = input("문자열 입력:")
my_list = inputvalue.split()
n = ""
find_word = input("단어 입력:")
for _ in my_list[::]:
    for find_word in my_list:
        n = my_list
    my_list.insert(n, find_word)




print(f"단어{find_word}의 출현 빈도:")