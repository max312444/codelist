# 키보드로부터 입력받은 한글 성별을 영어로 변환

# 성별을 한글로 입력하시오
comment = input("성별을 한글로 입력하세요(남자/여자) : ")
# 입력한 한글이 남자 이면 MAN을 출력 여자이면 WOMAN출력
if comment == ("남자"):
    print("MEN")
elif comment == ("여자"):
    print("WOMEN")
else:
    print("잘못된 입력힙니다.")