# 문자열 내 'h' 글자 개수 구하기
# for 문을 사용하여 아래 문자열 내 'h'의 개수를 출력하는 프로그램 작성

count = 0

myString = "hello hyundai hoho"
# 문자를 리스트에 대입
myString_list = list(myString)
# 리스트의 길이만큼의 범위에서 h가 들어가는지 확인
for i in range(len(myString_list)):
    if "h" == myString_list[i]:
        # 들어가면 count 1 더해주기
        count += 1

print("문자열 내 h 갯수 : ", count)   