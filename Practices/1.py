# 문제 구구단 출력 프로그램
# 사용자에게 메뉴 옵션을 출력
# 사용자로부터 입력을 받아 메뉴 선택
# 1을 선택한 경우, 사용자로 부터 구구단의 단(2~9)을 입력받음. 입력한 단이 유효하면 해당 단의 구구단을 출력
# 유효하지 않으면 오류 메시지 출력하고 다시 입력받음
# 프로그램 종료 : 2를 선택하면 종료
# 잘못된 입력 처리 : 1또는 2이외의 값이 입력된 경우 오류 메시지 출력후 메뉴 선텍으로 돌아감

while True: # 무한 반복
    print("------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("------------------")
    meun = int(input())
    if meun == 1: # 만약 메뉴가 1번일 때
        while True: # 반복문 작성
            number = int(input("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력\n"))
            if 9>= number >= 2: # 만약 number가 2~9 일 때
                for i in range(1, 10): # i의 범위 지정
                    print(f"{number}", "X" , f"{i}" , "=" ,(number * i)) # 곱셈 식 작성
                break # for 문에 break 걸면 곱셈 1행만 하고 멈춰 버려서 for문 앞인 while 문에 break를 걸어 잘못된 입력시에 단 입력 행으로 이동한다.
            else:
                print("2~9사이 정수를 입력해주세요") 
    elif meun == 2: # 만약 메뉴가 2번 일 때
        print("이용해주셔서 감사합니다.")
        break # 정지
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")

# while True:
#     print("-" * 10)
#     print("1. 구구단 출력")
#     print("2. 프로그램 종료")
#     print("-" * 10)
    
#     selected_meun = input("메뉴 값을 입력하세요 : ")
    
#     if selected_meun == "1":
#         dan = int(input("단을 입력하세요:"))
#         while True:
#             if 2 <= dan <= 9:
#               for num in range(1, 10):
#                 print(dan, "X", num, "=", dan * num)
                
#             break
        
#         print("단은 2~9사이의 정수 값 입력")
        
#     elif selected_meun == "2":
#         print("프로그램 종료")
#         break
#     else:
#         print("메뉴 값은 1 또는 2만 입력")
        