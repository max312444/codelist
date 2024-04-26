# 문제 11 패스워드 생성기
# 사용자로부터 길이를 입력받아 해당 길이의 무작위 패스워드를 생성하는 함수 구현
# 대문자 소문자 숫자 조합하여 생성

import random # 파이썬에 내장된 random 함수를 가져온다.

def total_password(length): # password 함수 정의
    upperletters = 'QWERTYUIOPASDFGHJKLZXCVBNM' # 대문자 리스트
    lowerletters = upperletters.lower() # 소문자 리스트
    numbers = '0123456789' # 숫자 리스트

    total = upperletters + lowerletters + numbers # 조합하는 식
    
    password = "" # 처음 password는 초기상태로 돌림
    
    for _ in range(length): # 범위 지정 식
        password += random.choice(total) # password를 랜덤으로 뽑아서 더한다.
        
    check1 = False # 대문자 유무
    check2 = False # 소문자 유무
    check3 = False # 숫자 유무
    # 비밀번호 검증
    for char in upperletters: # 대문자가 있으면 참이므로 정지
        if char in password:
            check1 = True
            break
        
    for char in lowerletters: # 소문자가 있으면 참이므로 정지
        if char in password:
            check2 = True
            break
        
    for char in numbers: # 숫자가 있으면 참이므로 정지
        if char in password:
            check3 = True
            break
        
    if check1 and check2 and check3: # 만약 대문자 소문자 숫자가 다 있다면 
        return password # 그 값을 가져옴
    else:
        return total_password(length) # 아니라면 다시 올라감

password_length = int(input("패스워드의 길이를 입력하세요: "))

if password_length >= 3: # 비밀번호가 3자리 이하인 경우 정지
    total_passwords = total_password(password_length)
    print(total_passwords)
else:
    print("비밀번호를 출력 할 수 없습니다.")
    
    
