# 문제 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
user_input = input().lower()
user_list = list(user_input)
count_list = []

for i in user_list:
    count = user_input.count[i]
    count_list.append(count)

if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(user_list[(count_list.index(max(count_list)))].upper())
    
