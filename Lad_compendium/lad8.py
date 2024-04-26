# 영문 모음 판별기

# inputValue 에 문자를 입력한다.
inputValue = input("한 문자를 입력하세요: ")
# a, e, i, o, u 에 대해 포함 하는지 판별한다. '포함 한다면 모음입니다.', '포함하지 않는다면 모음이 아닙니다.' 출력한다.
if inputValue == "a" or inputValue == "e" or inputValue == "i" or inputValue == "o" or inputValue == "u":
    print(inputValue,"는 모음입니다.")
else:
    print(inputValue,"는 모음이 아닙니다.")