# 문자열 내 단어 개수 출력
# for문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로그램 작성

myString = "It is a great weather with you"
# 공백을 기준으로 구분
words = myString.split()
count = 0
# 문장 내에 단어가 있는지 판별
for word in words:
    # 단어가 있으면 count하나 추가
    count += 1

print("문자열 단어 갯수 : ", count)