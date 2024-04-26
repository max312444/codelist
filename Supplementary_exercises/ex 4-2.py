#문제 4-2 비밀번호 검증기
#입력받은 비밀번호가 안전한지 검증하는 프로그램 작성
#조건 : 8자이상, 적어도 하나의 숫자포함, 적어도 하나의 대문자 포함
#하나라도 충족될땐 "비밀번호가 안전합니다." 충족되지 않을땐 "비밀번호가 안전하지 않습니다." 출력

password = input("비밀번호를 입력하세요: ") # 비밀번호가 8자리 이상일 때
if len(password) >= 8: # 숫자가 적어도 하나 들어가는지 판별
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
            
    has_uppercase = False # 대문자가 적어도 하나 들어가는지 판별
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    if has_number == True and has_uppercase ==True: # 둘다 충족할 때 비밀번호가 안전합니다. 출력
        print("비밀번호가 안전합니다.")
    else:
        print("비밀번호가 안전하지 않습니다.") # 둘다 충족하지 않을 때 비밀번호가 안전하지 않습니다. 출력
else:
    print("비밀번호가 안전하지 않습니다.") # 비밀번호가 8자리가 아닐 때 비밀번호가 안전하지 않습니다. 출력
